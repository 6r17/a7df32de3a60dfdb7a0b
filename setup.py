from setuptools import find_packages, setup

setup(
    name="a7df32de3a60dfdb7a0b",
    version="0.13.14",
    packages=find_packages(),
    install_requires=[
        "exorde_data",
        "aiohttp",
        "python-dotenv",
        "selenium==4.2.0",
        "pathlib",
        "requests"
    ],
    extras_require={"dev": ["pytest", "pytest-cov", "pytest-asyncio"]},
)
