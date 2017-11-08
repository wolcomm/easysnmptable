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
"""easysnmptable session module."""

from __future__ import print_function
from __future__ import unicode_literals

import easysnmp

from easysnmptable.table import Table


class Session(easysnmp.Session):
    """SNMP session handler class."""

    def __init__(self, *args, **kwargs):
        """Initialize Session instance."""
        super(self.__class__, self).__init__(*args, **kwargs)

    def gettable(self, oids, **kwargs):
        """Retrieve SNMP table contents."""
        varbinds = self.bulkwalk(oids, **kwargs)
        table = Table(varbinds=varbinds)
        return table

    def __enter__(self):
        """Enter context."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context."""
        del(self)
