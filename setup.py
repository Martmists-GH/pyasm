from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyasm",
    version="1.1.0",
    author="Martmists",
    author_email="martmists@gmail.com",
    description="A low-level library for manipulating Python Bytecode in an easy way.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License"
    ],
    packages=["asm", "asm.ops"],
    python_requires=">=3.5",
)
