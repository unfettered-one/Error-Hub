from setuptools import setup, find_packages

setup(
    name="errorhub",
    description="Error and Exception Handling lib",
    author="Yash Pakhale",
    author_email="pakhaleyash7@gmail.com",
    url="https://github.com/unfettered-one/Error-Hub.git",
    version="0.1.9",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.116.1",
        "pydantic==2.11.7",
        "dotenv==0.9.9",
        "requests==2.32.5",
        "pylint",
        "build==1.3.0",
        "twine==6.1.0",
    ],
    entry_points={
        "console_scripts": [],
    },
)
