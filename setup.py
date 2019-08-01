import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart_pipeline",
    version="0.0.1",
    author="Viktor Kirillov",
    author_email="kirillovmr@gmail.com",
    description="Data Pipeline for your Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirillovmr/python-pipeline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)