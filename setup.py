#!/usr/bin/python3
from setuptools import setup

setup(
    name="aurora-be",
    version="1.0",
    packages=["api", "models"],
    py_modules=["db_setup"]
)
