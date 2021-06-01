from setuptools import setup, find_packages

setup(
    name="pyskel",
    version="1.0",
    description="Skeleton python project",
    author="Sample Author",
    author_email="sample@example.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ['pyskel=pyskel.__main__:main']
    }
)