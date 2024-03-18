from setuptools import setup, find_packages

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='local_picbed_mac',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        "local_picbed_mac": ["data/*"],
    },
    install_requires=[
        "rumps",
        "flask",
        "pyobjc",
    ],
    author='ErwinLiYH',
    author_email='erwinli@qq.com',
    description='A minimalist local picbed for Mac OS',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
)