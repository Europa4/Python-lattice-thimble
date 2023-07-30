import numpy as np
import json

class Lattice:
    number_of_time_points = 0
    number_of_spacial_points = np.array([0, 0, 0])
    _total_number_of_points = 0
    time_separation = 0
    space_separation = np.array([0, 0, 0])

    def calculate_total_number_of_points(self):
        """Calculates the number of points in the lattice. Note that it takes into account the reduction due to
        Mou's formulation"""
        self.total_number_of_points = (2*self.number_of_time_points - 4)*np.prod(self.number_of_spacial_points)
    @property
    def total_number_of_points(self):
        return self._total_number_of_points

    @total_number_of_points.setter
    def total_number_of_points(self, value):
        if value > 0:
            self._total_number_of_points = value
        else:
            self._total_number_of_points = 0

    @property
    def number_of_time_points(self):
        return self._number_of_time_points

    #really not a big fan of the way I've done this
    def __eq__(self, other):
        if not isinstance(other, Lattice):
            return NotImplemented
        return (self.number_of_time_points == other.number_of_time_points and
                np.array(self.number_of_spacial_points == other.number_of_spacial_points).all() and
                self.total_number_of_points == other.total_number_of_points and
                self.time_separation == other.time_separation and
                np.array(self.space_separation == other.space_separation).all())

    def __init__(self, file_location = None):
        if file_location is None:
            return
        if type(file_location) is str:
            if file_location[:-5] != ".json":
                file_location += ".json"
            with open(file_location, 'r') as openfile:
                json_object = json.load(openfile)
                self.number_of_time_points = json_object["timePoints"]
                self.number_of_spacial_points = np.array(json_object["spacePoints"])
                self.time_separation = json_object["timeSeparation"]
                self.space_separation = np.array(json_object["spaceSeparation"])
        else:
            print("file_location should be a string")
    def save_to_file(self, file_location):
        if type(file_location) is str:
            if file_location[:-5] != ".json":
                file_location += ".json"
            pre_json_dict = {"timePoints" : self.number_of_time_points,
                             "spacePoints" : self.number_of_spacial_points.tolist(),
                             "timeSeparation" : self.time_separation,
                             "spaceSeparation" : self.space_separation.tolist()}
            json_object = json.dumps(pre_json_dict, indent=4)
            with open(file_location, "w") as outfile:
                outfile.write(json_object)
        else:
            print("file_location should be a string")