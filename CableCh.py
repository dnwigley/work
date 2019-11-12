# Electrical BS7671 Formula classes
# BS7671:2018
# Author: David Wigley
# Version: 1.0 draft
from math import sqrt


class CableCh:
    """Clause 5.6 Page 381 Harmonic currents in line conductors"""

    def __init__(self, ifun=1, h3=1, h5=1, h7=1, h9=1):
        """Initialize cable variables"""
        self.Ifun = ifun
        self.h3 = h3
        self.h5 = h5
        self.h7 = h7
        self.h9 = h9

    def ch(self):
        """Clause 5.6 Page 381 Harmonic currents in line conductors"""
        self.Ch = sqrt(
            (
                self.Ifun ** 2
                + self.h3 ** 2
                + self.h5 ** 2
                + self.h7 ** 2
                + self.h9 ** 2
            )
            / self.Ifun ** 2
        )

        return self.Ch


# calling the class
my_cable = CableCh(ifun=10, h3=3, h5=5, h7=2, h9=2)


# printing out values for checking

print("\nYour Ch factor is " + str(my_cable.ch()))
