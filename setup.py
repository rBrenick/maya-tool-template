import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RAW_TOOL_NAME",
    version="1.0.0",
    author="Richard Brenick",
    author_email="RichardBrenick@gmail.com",
    description="maya tool template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rBrenick/RAW_TOOL_NAME",
    packages=setuptools.find_packages(),
    package_data={'': ['*.*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    install_requires=[
    "Qt.py",
    ]
)