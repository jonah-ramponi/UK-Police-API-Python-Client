from setuptools import setup, find_packages

setup(
    name="uk_police_client",
    version="0.1",
    packages=find_packages(),
    install_requires=["httpx", "pydantic", "python-dateutil"],
)
