

Setup server:
https://pypi.org/project/pypiserver/

"""
pip install pypiserver                # Or: pypiserver[passlib,cache]
mkdir ~/packages                      # Copy packages into this directory.
pypi-server run -p 8080 ~/packages &    
"""

Build:

python setup.py sdist bdist_wheel

Copy to ~/packages for https://pypi.org/project/pypiserver/

verysimplemoduleliam_package-0.1.0-py3-none-any.whl
verysimplemoduleliam_package-0.1.0.tar.gz


Install:

pip install --index-url http://localhost:8080/simple/ verysimplemoduleliam_package

Example:

"""

from verysimplemoduleliam import *
add(50,12)
Mammals().printMembers()
Number(20).val()

import verysimplemoduleliam as F
g = F.Number(10)
g.val()
F.Number(20).val()
F.Mammals().printMembers()
"""

Resources:
* https://pypi.org/project/example-pypi-package/#description
* https://pypi.org/project/pypiserver/
* https://www.freecodecamp.org/news/build-your-first-python-package/


