import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helping",
    version="0.0.3",
    author="Ronald Hayden",
    author_email="ron@conquerprogramming.com",
    description="Readable information for real people.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ConquerProgramming1/helping",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
