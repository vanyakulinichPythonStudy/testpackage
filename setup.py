import setuptools

from setuptools.command.develop import develop
from setuptools.command.install import install

with open("README.md", "r") as fh:
    long_description = fh.read()


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        print('PACKAGE SUCCESSFULLY INSTALLED')
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        print('PACKAGE SUCCESSFULLY INSTALLED2')
        install.run(self)


setuptools.setup(
    name="testpkg",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'testpkg=testpkg.command_line:main'
        ]
    },
    python_requires='>=3.5',
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)

"""
https://packaging.python.org/tutorials/packaging-projects/ //tutorial about packages
# 
https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html //cmd-scripts
# 
req packages before setups:
sudo python -m pip install --upgrade pip setuptools wheel
sudo python -m pip install tqdm
sudo python -m pip install --user --upgrade twine
# 
python3 setup.py sdist bdist_wheel //package
# 
sudo pip3 install dist/testpkg-0.0.1.tar.gz //install local package

"""
