# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from field import Field
from interaction import Interaction
if __name__ == '__main__':
    phi = Field("phi")
    chi = Field("chi")
    first_interaction = Interaction()
    first_interaction.add_field(phi)
    first_interaction.add_field(chi)
    phi.rename_field("gamma")
    first_interaction.print_field_names()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
