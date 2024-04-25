# Copyright 2024 University of Pittsburgh
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#
# Authors:  John Aronis

class Patient:
    """Patient class."""

    def __init__(self,fields,values):
        self.field_values = dict()
        for i in range(len(fields)): self.field_values[fields[i]] = values[i]

    def get_value(self,field): return self.field_values[field]

    def set_value(self,field,value): self.field_values[field] = value

    def __repr__(self):
        return self.get_value('RSVLABRESULT')

