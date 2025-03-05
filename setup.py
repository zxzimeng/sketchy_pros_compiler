from setuptools import setup, find_packages

setup(
    name="sketchy_pros_compiler",
    version="1.0.1",
    scripts=['pros_sketchy'],
    description="A build system wrapper for PROS robotics projects",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Zimeng Xiong",
    url="https://github.com/zxzimeng/sketchy_pros_compiler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)