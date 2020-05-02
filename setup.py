import setuptools

with open('VERSION', 'r') as fh:
    version = fh.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="infratools",
    version=version,
    install_requires=[
      "setuptools",
      "wheel",
      "tqdm",
      "twine",
      "boto3"
    ],
    author="Daniel Barragan",
    author_email="dbarragan1331@gmail.com",
    description="Collection of infrastructure tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/d4n13lbc/infratools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)