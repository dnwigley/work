"""Electrical BS7671 Formula classes
#BS7671:2018
#Author: David Wigley
#Version: 1.0 draft"""


class CableITNoOverLoad:
    """Clause 5.2 Page 378 Where no overload protection is required"""

    def __init__(self, ca=1, cs=1, cd=1, ib=1, ci=1, cf=1, cc=1, cg=1):

        """Initialize cable variables"""

        self.Cg = cg
        self.Ca = ca
        self.Cs = cs
        self.Cd = cd
        self.Ides = ib
        self.Ci = ci
        self.Cc = cc

    def ch(self):

        self.It = self.Ides / (
            self.Cg * self.Ca * self.Cs * self.Cd * self.Ci * self.Cc
        )
        return self.It


# calling the class

my_cable = CableITNoOverLoad(ca=1, cs=1, cd=1, ci=1, cc=1, cg=1, ib=100)


# printing out values for checking


print(
    "\nYour It where overload protection is not required "
    + str(my_cable.it_no_overload())
)
