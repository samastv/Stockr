"""
Insta485 python package configuration.

Andrew DeOrio <awdeorio@umich.edu>
"""

from setuptools import setup

setup(
    name='insta485',
    version='0.1.0',
    packages=['insta485'],
    include_package_data=True,
    install_requires=[
        'arrow==0.13.0',
        'bs4==0.0.1',
        'Flask==1.0.2',
        'Flask-Testing==0.7.1',
        'html5validator==0.3.1',
        'nodeenv==1.3.3',
        'pycodestyle==2.4.0',
        'pydocstyle==3.0.0',
        'pylint==2.2.2',
        'pytest==4.1.1',
        'requests==2.21.0',
        'selenium==3.141.0',
        'sh==1.12.14',
    ],
)
