from setuptools import setup, find_packages

setup(
    name="errorhub",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["fastapi==0.116.1", "pydantic==2.11.7", "dotenv==0.9.9", "requests==2.32.5"],
    entry_points={
        "console_scripts": [],
    },
)
