from setuptools import setup, find_packages

setup(
    name="project_package",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "nbformat>=5.0.0",
        "nbclient>=0.5.0"
    ],
    description="Community Risk Intelligence Agent package",
    author="Md Kamran Akhter",
    license="MIT"
)
