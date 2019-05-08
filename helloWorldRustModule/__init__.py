def __build():
    from setuptools import setup
    from setuptools_rust import RustExtension
    import os, glob, sys

    PYTHON_MAJOR_VERSION = sys.version_info[0]

    cwd_bup = os.getcwd()

    try:
        modulePath = os.path.dirname(os.path.realpath(__file__))
        print("Building library '" + os.path.basename(modulePath) + "' ...")
    
        os.chdir(modulePath)
    
        setup(name='__lib',
              rust_extensions=[RustExtension(
                '__lib',
                '__src/Cargo.toml',
                debug=False,
                rustc_flags=['--cfg=Py_{}'.format(PYTHON_MAJOR_VERSION)],
                features=['numpy/python{}'.format(PYTHON_MAJOR_VERSION)],
              )],
              script_args=["-q", "build_ext", "--inplace"])

    finally:
        os.chdir(cwd_bup)

__build()

from .__src.wrappers import *
