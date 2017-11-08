[![PyPI](https://img.shields.io/pypi/v/easysnmptable.svg)](https://pypi.python.org/pypi/easysnmptable)
[![Build Status](https://travis-ci.org/wolcomm/easysnmptable.svg?branch=master)](https://travis-ci.org/wolcomm/easysnmptable)
[![codecov](https://codecov.io/gh/wolcomm/easysnmptable/branch/master/graph/badge.svg)](https://codecov.io/gh/wolcomm/easysnmptable)
[![Code Health](https://landscape.io/github/wolcomm/easysnmptable/master/landscape.svg?style=flat)](https://landscape.io/github/wolcomm/easysnmptable/master)
[![Requirements Status](https://requires.io/github/wolcomm/easysnmptable/requirements.svg?branch=master)](https://requires.io/github/wolcomm/easysnmptable/requirements/?branch=master)

# easysnmptable

An extension to [easysnmp](https://github.com/kamakazikamikaze/easysnmp) providing:
- SNMP Table handling
- Context manager support

## Installation

```bash
$ pip install easysnmptable
```

## Usage

```python
from easysnmptable import Session

with Session(hostname='localhost', community='public', version=2) as session:
  iftable = session.gettable('ifTable')

for index, row in table.rows.items():
  print("index: {}".format(index))
  for key, value in row.items():
    print("{}: {}".format(key, value))
```
