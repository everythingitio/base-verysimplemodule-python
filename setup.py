from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'My first Python package math utls'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description math utils add minus divide multiple'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="verysimplemoduleliam_package", 
        version=VERSION,
        author="Verysimplemodule Liam",
        author_email="<verysimplemoduleliam@verysimplemoduleliam.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)