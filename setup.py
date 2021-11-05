from setuptools import setup, find_packages

setup(
    name="ApexTrackerPy",
    author="nerrog",
    version="1.0",
    description="Library for easily calling Apex tracker APIs (supports TRN and APEX LEGENDS APIs)",
    install_requires=["requests"],
    packages=find_packages()
)