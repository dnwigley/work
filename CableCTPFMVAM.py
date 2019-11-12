"""Electrical BS7671 Formula classes
#BS7671:2018
#Author: David Wigley
#Version: 1.0 draft"""

from math import sqrt, cos, sin, radians


class CableCTPFMVAM():
	"""Clause 6.3 Page 382 Correction for operating temperature and power 
	factor"""
	

	def __init__(
				self, 
				pf=1,
				mvamr=0,
				mvamx=0
				):
		"""Initialize cable variables"""
	
		self.Ct = 1
		self.Pf = pf
		self.mVAmr = mvamr
		self.mVAmx = mvamx
		self.mVAmz = 1
		
	def ctpf(self):

		Ct = self.Ct
		
		if self.mVAmx == 0:
			self.mVAmz = Ct * cos(radians(self.Pf)) * self.mVAmr
			return self.mVAmz
		else:
			self.mVAmz = (Ct *
			cos(radians(self.Pf)) *
			self.mVAmr +
			sin(radians(self.Pf)) *
			self.mVAmx)
			return self.mVAmz
		
# calling the class		
my_cable = CableCTPFMVAM(
					pf=0.8, 
					mvamr=11, 
					mvamx=13)


# printing out values for checking

print("\nYour CT * Pf * mV/A/m is " + str(my_cable.ctpf()))