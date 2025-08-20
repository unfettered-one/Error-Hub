from setuptools import setup, find_packages

setup(
    name="errorhub",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "dotenv"

    ],
    entry_points={
        "console_scripts": [],
    },
)
