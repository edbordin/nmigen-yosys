from setuptools import setup, find_packages


def version():
    from setuptools_scm.git import parse as parse_git

    yosys_git = parse_git("yosys")
    if yosys_git.exact:
        yosys_version = yosys_git.format_with("{tag}")
    else:
        yosys_version = yosys_git.format_with("{tag}.post{distance}")

    package_git = parse_git(".")
    package_version = package_git.format_with(".dev{distance}")

    return yosys_version + package_version


def long_description():
    with open("README.rst") as f:
        return f.read()


setup(
    name="nmigen-yosys",
    version=version(),
    author="whitequark",
    author_email="whitequark@whitequark.org",
    description="Custom WebAssembly build of Yosys used by nMigen as a fallback",
    long_description=long_description(),
    license="ISC", # same as Yosys
    setup_requires=["setuptools_scm", "wheel"],
    install_requires=["wasmtime~=0.15.1"],
    packages=["nmigen_yosys"],
    package_data={"nmigen_yosys": ["yosys.wasm"]},
    project_urls={
        "Source Code": "https://github.com/nmigen/nmigen-yosys",
        "Bug Tracker": "https://github.com/nmigen/nmigen-yosys/issues",
    },
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
)
