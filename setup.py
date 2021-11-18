from setuptools import setup, find_packages

setup(
    name="ApexTrackerPy",
    author="nerrog",
    version="1.8",
    url="https://github.com/nerrog/ApexTrackerPy",
    long_description=open(('README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    description="Library for easily calling Apex tracker APIs (supports TRN and APEX LEGENDS APIs)",
    install_requires=["requests"],
    packages=find_packages()
)