from setuptools import setup

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)

setup(
    name="words",
    version=__version__,
    description="Tool to get a large collection of words.",
    url="https://github.com/Ceasar/words",
    license='MIT',
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    py_modules=['words'],
    scripts=['words.py'],
    include_package_data=True,
    keywords=["words", "dictionary", "lexicon"],
    classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    ],
    use_2to3=True,
)
