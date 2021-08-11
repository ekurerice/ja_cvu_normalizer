import os
import sys
from setuptools import find_packages, setup


def decomment(file):
    for row in file:
        if "==" in row:
            yield row
        continue


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        f = decomment(f)
        requirements = [line.rstrip() for line in f]
    print(requirements)
    return requirements


with open("README.md") as f:
    long_description = f.read()

setup(
    name="jp_cvu_normalizer",
    version="0.2.0",
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
