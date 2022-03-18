"""Setup configuration."""
import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysunpower",  # Replace with your own username
    version="0.1",
    author="Jeef",
    author_email="",
    license="MIT",
    description="A Python module to parse the unpublished RESTAPI of SunPower PVS6 Systems ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeeftor/pysunpower",
    packages=setuptools.find_packages(exclude=["tests*"]),
    install_requires=["pydantic", "asyncio", "aiohttp"],
    download_url="https://github.com/jeeftor/pysunpower/archive/refs/tags/0.1.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
