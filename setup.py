#!/usr/bin/env python
# Copyright 2017 Workonline Communications (Pty) Ltd. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Setup configuration script for easysnmptable."""

from __future__ import print_function
from __future__ import unicode_literals

from setuptools import find_packages, setup

descr = "An extension to easysnmp providing table handling and other features."

with open('packaging/VERSION') as f:
    version = f.read().strip()
with open('packaging/requirements.txt') as f:
    requirements = f.read().split("\n")

try:
    import pypandoc
    readme = pypandoc.convert_file('README.md', 'rst', format='md')
except (ImportError, RuntimeError) as e:
    print("README conversion failed: {}".format(e))
    readme = None


setup(
    name='easysnmptable',
    version=version,
    author='Workonline Communications',
    author_email='communications@workonkonline.co.za',
    description=descr,
    long_description=readme,
    license='Apache-2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    packages=find_packages(),
    include_package_data=True,

    url='https://github.com/wolcomm/easysnmptable',
    download_url='https://github.com/easysnmptable/%s' % version,

    install_requires=requirements,
)
