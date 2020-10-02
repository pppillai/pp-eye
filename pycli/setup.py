from setuptools import setup

setup(
    name='pycli',
    version='1.0',
    py_modules=['pycli'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        greet=pycli:greet
    ''',
)