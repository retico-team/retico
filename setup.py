#!/usr/bin/env python3

"""
Setup script.

Use this script to install the GoogleASR module of the retico simulation framework.
Usage:
    $ python3 setup.py install
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

exec(open("retico/version.py").read())

import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

config = {
    "description": "Retico is an open source framework for building state-of-the-art incremental processing systems.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "author": "Thilo Michael",
    "author_email": "uhlomuhlo@gmail.com",
    "url": "https://github.com/retico-team/retico",
    "download_url": "https://github.com/retico-team/retico",
    "python_requires": ">=3.6, <4",
    "version": __version__,
    "install_requires": [
        "retico-core~=0.2",
        "retico-googleasr~=0.1",
        "retico-googletts~=0.1",
        "retico-wav2vecasr~=0.1",
        "retico-speechbraintts~=0.1",
        "retico-hftranslate~=0.1",
    ],
    "packages": find_packages(),
    "name": "retico",
    "keywords": "retico, framework, incremental, dialogue, dialog, asr, speech",
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
}

setup(**config)
