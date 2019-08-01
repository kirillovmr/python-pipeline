import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart_pipeline",
    version="0.0.2",
    author="Viktor Kirillov",
    author_email="kirillovmr@gmail.com",
    description="Data Pipeline for your Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirillovmr/python-pipeline",
    packages=setuptools.find_packages(),
    install_requires=[
        'tqdm>=4.31.1',
    ],
    classifiers=[
        # How mature is this project? Common values are
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Information Technology',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",

        # Operating system
        "Operating System :: OS Independent",
    ],
)