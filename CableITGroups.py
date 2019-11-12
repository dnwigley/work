"""Electrical BS7671 Formula classes
#BS7671:2018
#Author: David Wigley
#Version: 1.0 draft"""

from math import sqrt


class CableITGroups:
    """Clause 5.1.2 page 378 determination of the size of cable to be used for
    groups of circuits"""

    def __init__(
        self,
        n=1,
        tp=1,
        ca=1,
        cs=1,
        cd=1,
        ib=1,
        it=1,
        ifun=1,
        ci=1,
        cf=1,
        cc=1,
        inom=1,
        pf=1,
        cg=1,
    ):
        """Initialize cable variables"""

        self.Cg = cg
        self.Ca = ca
        self.Cs = cs
        self.Cd = cd
        self.Ides = ib
        self.Ct = 1
        self.Ci = ci
        self.Cf = cf
        self.Cc = cc
        self.In = inom
        self.Eq2 = 1
        self.Eq3 = 1
        self.Eq4 = 1
        # self.It = it

    def it_groups(self):
        """Clause 5.1.2 page 378 determination of the size of cable to be used
        for groups of circuits"""

        self.Eq2 = self.In / (
            self.Cg * self.Ca * self.Cs * self.Cd * self.Ci * self.Cf * self.Cc
        )

        self.Eq3 = self.Ides / (
            self.Cg * self.Ca * self.Cs * self.Cd * self.Ci * self.Cf * self.Cc
        )

        self.Eq4 = (1 / (self.Ca * self.Cs * self.Cd * self.Ci)) * (
            sqrt(
                (self.In / (self.Cf * self.Cc)) ** 2
                + 0.48 * self.Ides ** 2 * ((1 - self.Cg ** 2) / self.Cg ** 2)
            )
        )

        # Which equation gives the highest result
        self.It = max(self.Eq2, self.Eq3, self.Eq4)
        return self.It


# calling the class
my_cable = CableITGroups(
    ca=1, cs=1, cd=1, it=300, ifun=10, ci=1, cf=1, cc=1, inom=100
)


print(
    "\nYour group It should be equal or greater than "
    + str(my_cable.it_groups())
)

print(
    "\nEquation 2 "
    + str(my_cable.Eq2)
    + " Equation 3 "
    + str(my_cable.Eq3)
    + " Equation 4 "
    + str(my_cable.Eq4)
)
