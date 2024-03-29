from setuptools import find_packages
from distutils.core import setup

VERSION = '0.0.4' 
DESCRIPTION = 'Package to interface Virginia Diodes PM5 Powermeter with Python'
LONG_DESCRIPTION = 'A package that uses pyvisa to interface with the Virginia Diodes PM5 terahertz powermeter, allowing for power readings and remote control via Python.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pyPM5", 
        version=VERSION,
        author="Matt Jamieson",
        author_email="<mjamieson21@outlook.com>",
        url = 'https://github.com/matt-jamieson/pyPM5',   
        download_url = 'https://github.com/matt-jamieson/pyPM5/archive/refs/tags/0.0.4.tar.gz', 
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pyvisa"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'terahertz','powermeter','PM5','Virginia Diodes'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
