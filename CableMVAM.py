"""Electrical BS7671 Formula classes
#BS7671:2018
#Author: David Wigley
#Version: 1.0 draft
from math import cos, sin, radians
#import math"""


class CableMVAM:
    """Clause 6.2 Page 382 Correction for load power factor"""

    def __init__(self, pf=1, mvamr=0, mvamx=0):

        """Initialize cable variables"""

        self.Pf = pf
        self.mVAmr = mvamr
        self.mVAmx = mvamx
        self.mVAmz = 1

    def mvam(self):
        """Clause 6.2 Page 382 Correction for load power factor"""
        self.mVAmz = (cos(radians(self.Pf)) * self.mVAmr) + (
            sin(radians(self.Pf)) * self.mVAmx
        )
        return self.mVAmz


# calling the class
my_cable = CableMVAM(pf=0.8, mvamr=11, mvamx=13)


# printing out values for checking


print("\nYour mVAmz is " + str(my_cable.mvam()))
