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
"""easysnmptable table module."""

from __future__ import print_function
from __future__ import unicode_literals


class Table(object):
    """SNMP Table result class."""

    def __init__(self, varbinds=[]):
        """Initialize Table instance."""
        self.cols = set()
        self.indices = set()
        self.rows = dict()
        for varbind in varbinds:
            self.cols.add(varbind.oid)
            self.indices.add(varbind.oid_index)
            cell = {varbind.oid: varbind.value}
            try:
                self.rows[varbind.oid_index].update(cell)
            except KeyError:
                self.rows[varbind.oid_index] = cell
