from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

name = "password_validator"
version = "0.1"

setup(
    name=name,
    version=version,
    description="A password validator that checks passwords against specified criteria.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("password_validator"),
    package_dir={"":"password_validator"},
    url="https://github.com/juzor/password-validator",
    author="Justice Uzor",
    author_email="chigozirim.uzor@outlook.com",
    license="MIT",
    keywords= "password, validator, rules",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ],
    python_requires=">=3.8",
)