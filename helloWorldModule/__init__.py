from distutils.core import setup as __setup
from distutils.core import Extension as __extension
import os as __os
import glob as __glob

def __build():
    cPath = __os.path.dirname(__os.path.realpath(__file__))
    print("Building library '" + __os.path.basename(cPath) + "' ...")

    pwd_bup = __os.getcwd()
    __os.chdir(cPath)

    sources = __glob.glob('__src/*.c')
    #print("   Sources:", sources)

    module1 = __extension('__lib',
                          sources=sources)

    __setup(name='__lib',
            ext_modules=[module1],
            script_args=["build_ext", "--inplace"])

    __os.chdir(pwd_bup)

__build()

from .__src.wrappers import *
