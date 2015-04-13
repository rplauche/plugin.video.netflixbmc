"""
## Multiple platform selector for pyOpenSSL binary distributions
# Original from: https://pypi.python.org/pypi/pyOpenSSL/0.13
# Note: Version 0.14 switches to pure python relying on cryptographic
#  library which relies on cffi (amongst other things). A similar
#  pattern to this could probably be followed for it's binary
#  modules if and upgrade is ever required.

## To add new platform:
# Ensure python compatible toolchain is installed
# extract pyOpenSSL-0.13.tar.gz
# Ensure you run the same version of python used in kodi on your platform.

cd pyOpenSSL-0.13
python -c "import setuptools; execfile('setup.py')" bdist_egg
cp dist/pyOpenSSL-0.13-*.egg ../
cd ../
for filename in *.egg; do
 mkdir "${filename%.*}"
 unzip $filename -d "${filename%.*}"
 rm $filename
done

# and then add a suitable match -> path append below
# Please do contribute added distributions back to project!
"""

import os
import sys
import platform

paths = [os.path.dirname(__file__)]

identifier1 = (platform.system(), platform.architecture()[0]) + platform.python_version_tuple()[0:2]

## Platform Identifiers
if identifier1 == ('Darwin', '64bit', '2', '6'):
    paths.append(os.path.join(os.path.dirname(__file__), "pyOpenSSL-0.13-py2.6-macosx-10.10-intel"))

elif identifier1 == ('Windows', '32bit', '2', '6'):
    paths.append(os.path.join(os.path.dirname(__file__), "pyOpenSSL-0.13-py2.6-win32"))

elif identifier1 == ('Windows', '32bit', '2', '7'):
    paths.append(os.path.join(os.path.dirname(__file__), "pyOpenSSL-0.13-py2.7-win32"))

elif identifier1 == ('Linux', '32bit', '2', '7'):
    identifier2 = identifier1 + platform.libc_ver()

    if identifier2 == ('Linux', '64bit', '2', '7', 'glibc', '2.4'):
        raise NotImplementedError
else:
    print "OpenSSL distribution not available for your platform. \nPlease add one if possible by following instructions in top of file: " + str(__file__)

# Add required paths to python search path
for p in paths:
    if p not in sys.path:
        sys.path.append(p)

import OpenSSL