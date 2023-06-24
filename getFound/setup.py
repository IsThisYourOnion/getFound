from setuptools import setup, find_packages

setup(
    name='getFound',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'getFound = getFound.main:main'
        ]
    },
)
