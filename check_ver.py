# run:
# python check_ver.py > versions.txt
import os
import pyspecdata
import pyspecProcScripts
import Instruments
import SpinCore_pp
import sys
def dos2mingw(x):
    return os.path.split(os.path.normpath(x))[0].replace('C:\\','\\c\\').replace('\\','/')
for thismodule in [pyspecdata, pyspecProcScripts,Instruments,SpinCore_pp]:
    print(thismodule.__name__)
    print("\n\tlocation -->",thismodule.__file__,end="")
    os.chdir(dos2mingw(thismodule.__file__))
    print("\n\tbranch: ",end="")
    sys.stdout.flush()
    os.system('git rev-parse --abbrev-ref HEAD')
    print("\n\thash: ",end="")
    sys.stdout.flush()
    os.system('git rev-parse @')

