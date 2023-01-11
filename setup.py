from setuptools import setup

setup(
    name='app',
    version='0.1.0',
    py_modules=['app'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'app = app:cli',
        ],
    },
)
