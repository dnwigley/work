"""Electrical BS7671 Formula classes
#BS7671:2018
#Author: David Wigley
#Version: 1.0 draft"""
from math import sqrt


class CableCg:
    """Number of circuits in the group Clause 2.3.3.1 Page 375 Groups in
    conduit Systems, cable trunking systems or cable ducting systems"""

    def __init__(self, n=1):
        """Initialize cable variables"""
        self.n = n

    def cg(self):

        self.Cg = 1 / sqrt(self.n)
        return self.Cg


# calling the class
my_cable = CableCg(2)  # Insert number of cables in group

# printing out values for checking
print("\nYour Cg factor is " + str(my_cable.cg()))
