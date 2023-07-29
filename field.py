import numpy as np


class Field:
    name = ""

    def __init__(self, name):
        self.name = name

    def rename_field(self, new_name):
        self.name = new_name
