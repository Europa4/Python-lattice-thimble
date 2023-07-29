import numpy as np
from field import Field

class Interaction:
    fields = np.array([], dtype=Field)

    def add_field(self, field):
        self.fields = np.append(self.fields, field)

    def print_field_names(self):
        for field in self.fields:
            print(field.name)
