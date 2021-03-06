import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cloudfile",
    version="0.2.10",
    description="Upload and restore large files in the intented location.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/takotab/cloudfile",
    author="Tako Tabak",
    author_email="takotabak@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cloudfile", "cloudfile/google"],
    include_package_data=True,
    install_requires=["wget", "fire"],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)
