#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

package_name = "culqi"
package_path = os.path.abspath(os.path.dirname(__file__))
repositorty_url = "https://github.com/culqi/culqi"
long_description_file_path = os.path.join(package_path, "README.md")
long_description = ""

try:
    with open(long_description_file_path) as f:
        long_description = f.read()
except IOError:
    pass


setup(
    name=package_name,
    packages=find_packages(exclude=[".*", "docs", "scripts", "tests*", "legacy",]),
    include_package_data=True,
    version=__import__("culqi").__version__,
    description="""Biblioteca de Culqi en Python""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Willy Aguirre, Joel Ibaceta, Martin Josemaría",
    zip_safe=False,
    keywords=["Api Client", "Payment Integration", "Culqi", "Python 3", "Python 2",],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url=repositorty_url,
    download_url="%(url)s/-/archive/%(version)s/%(package)s-%(version)s.tar.gz"
    % {
        "url": repositorty_url,
        "version": __import__("culqi").__version__,
        "package": package_name,
    },
    requires=["requests",],
    install_requires=["requests",],
)
