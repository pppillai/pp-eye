from setuptools import setup

setup(
    name='pycli',
    version='1.0',
    author='pradeep',
    py_modules=['pycli'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        hello=pycli:hello
    ''',
)