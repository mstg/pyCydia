import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyCydia",
    version = "1.0.3",
    author = "switchpwn",
    author_email = "mustiigezen@gmail.com",
    description = ("Cydia API wrapper for Python"),
    license = "MIT",
    keywords = "cydia api python wrapper",
    url = "https://github.com/switchpwn/pyCydia",
    download_url = "https://github.com/switchpwn/pyCydia/tarball/1.0",
    packages=['pycydia'],
    long_description = read("README.rst"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
