"""Electrical BS7671 Formula classes
#BS7671:2018
#Author: David Wigley
#Version: 1.0 draft"""


class CableItSingleCcts:
    """Clause 5.1.1 page 377 determination of the size of cable to be used for
    single circuits """

    def __init__(self, ca=1, cs=1, cd=1, ci=1, cf=1, cc=1, inom=1):
        """Initialize cable variables"""

        self.Ca = ca
        self.Cs = cs
        self.Cd = cd
        self.Ci = ci
        self.Cf = cf
        self.Cc = cc
        self.In = inom

    def it_single_ccts(self):
        """"""
        self.It = self.In / (
            self.Ca * self.Cs * self.Cd * self.Ci * self.Cf * self.Cc
        )
        return self.It


# calling the class
my_cable = CableItSingleCcts(ca=1, cs=1, cd=1, ci=1, cf=0.75, cc=1, inom=100)


print(
    "\nYour single It should be equal or greater than "
    + str(my_cable.it_single_ccts())
)
