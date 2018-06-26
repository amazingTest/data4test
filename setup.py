import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data4test",
    version="1.0.0",
    author="Yuyi Shao",
    author_email="523314409@qq.com",
    description="data for test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amazingTest/data4test",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)