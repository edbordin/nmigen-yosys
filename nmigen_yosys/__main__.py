import sys, pkg_resources, wasmtime

wasi_cfg = wasmtime.WasiConfig()
wasi_cfg.set_argv(["yosys", *sys.argv[1:]])
wasi_cfg.preopen_dir(".", ".")
wasi_cfg.inherit_stdin()
wasi_cfg.inherit_stdout()
wasi_cfg.inherit_stderr()

store = wasmtime.Store()
linker = wasmtime.Linker(store)
wasi = linker.define_wasi(wasmtime.WasiInstance(store,
    "wasi_snapshot_preview1", wasi_cfg))
yosys = linker.instantiate(wasmtime.Module(store,
    pkg_resources.resource_string(__name__, "yosys.wasm")))
yosys.get_export("_start")()
