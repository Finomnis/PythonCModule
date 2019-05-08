def __build():
    from distutils.core import setup
    from distutils.core import Extension
    import os
    import glob

    cwd_bup = os.getcwd()

    try:
        modulePath = os.path.dirname(os.path.realpath(__file__))
        print("Building library '" + os.path.basename(modulePath) + "' ...")
    
        os.chdir(modulePath)
    
        sources = glob.glob('__src/**/*.c', recursive=True)
        #print("   Sources:", sources)
    
        module1 = Extension('__lib',
                              sources=sources)

        setup(name='__lib',
                ext_modules=[module1],
                script_args=["-q", "build_ext", "--inplace"])

    finally:
        os.chdir(cwd_bup)

__build()

from .__src.wrappers import *
