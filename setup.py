import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyxi",
    version="0.0.1",
    author="Phoenix Logan",
    author_email="phoenix.logan@czbiohub.org",
    description="xi correlation for tied data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/czbiohub/pyxi/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
