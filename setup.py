import os
import sys
from setuptools import find_packages, setup

def read_requirements():
    import json
    pipfile_lock = json.load(open(os.path.join('.', 'Pipfile.lock')))
    return list(pipfile_lock["default"].keys())

with open("README.md") as f:
    long_description = f.read()
    try:
        from m2r import convert
        long_description = convert(long_description)
    except:
        pass

setup(
    name="jp_cvu_normalizer",
    version="0.2.4.1",
    author="ekurerice",
    long_description=long_description,
    url="https://github.com/ekurerice/jp_cvu_normalizer",
    author_email="alexandria.rindybell@gmail.com",
    packages=find_packages(exclude=["test"]),
    package_data={
        "jp_cvu_normalizer": ["resource/*"]
    },
    include_package_data=True,
    install_requires=read_requirements(),
    python_requires='>=3.6',
)
