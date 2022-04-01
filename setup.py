import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-sample-package",
    version="0.0.1",
    author="Tristan Nolde",
    author_email="author@example.com",
    description="A Python sample package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TrisNol/python-sample-package",
    project_urls={
        "Bug Tracker": "https://github.com/TrisNol/python-sample-package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
