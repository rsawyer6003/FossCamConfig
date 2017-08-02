from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.comand.test import test as TestCommand
import io
import codecs
import os
import sys

import FossCamConfig

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='FossCamConfig',
    version=sandman.__version__,
    url='http://github.com/rsawyer6003/FossCamConfig/',
    license='GNU General Public License V3',
    author='Ryan Sawyer',
    tests_require=['pytest'],
    install_requires=['WSDiscovery>=0.2',
                    'netifaces>=1.0',
                    ],
    cmdclass={'test': PyTest},
    author_email='ryan@sealarm.net',
    description='Camera Configuration Tool For ONVIF Cameras',
    long_description=long_description,
    packages=['FossCamConfig'],
    include_package_data=True,
    platforms='any',
    test_suite='FossCamConfig.test.test_FossCamConfig',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Linux',
        'Intended Audience :: Camera Installers',
        'License :: OSI Approved :: GPL3',
        'Operating System :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules',
    extras_require={
        'testing': ['pytest'],
    }
)
