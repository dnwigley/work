#Electrical BS7671 Formula classes
#BS7671:2018
#Authors: David Wigley, Harshit Mahida
#Version: 1.1 draft
from math import sqrt, cos, sin, radians
#import math
class CableCalc:
	"""Cable calculations for me"""
	

	def __init__(self, n = 1, tp = 1,
					ca = 1, cs = 1, cd = 1, 
					ib =  1, it = 1, ifun = 1, 
					h3 = 1, h5 = 1, h7 = 1, 
					h9 = 1, ci = 1, cf = 1,
					cc =1, inom = 1, pf = 1,
					mvamr = 0, mvamx = 0
				):
		"""Initialize cable variables"""
		
		
		self.n = n 
		self.Cg = 1
		self.Tp = tp
		self.Ca = ca
		self.Cs = cs
		self.Cd = cd
		self.Ides = ib
		self.It = it
		self.Ct = 1
		self.Ch = 1
		self.Ifun = ifun
		self.h3 = h3
		self.h5 = h5
		self.h7 = h7
		self.h9 = h9
		self.Ci = ci
		self.Cf = cf
		self.Cc = cc
		self.In = inom
		self.Eq2 = 1
		self.Eq3 = 1
		self.Eq4 = 1
		self.Pf = pf
		self.mVAmr = mvamr
		self.mVAmx = mvamx
		self.mVAmz = 1
		
	def cg(self):
		"""Number of circuits in the group Clause 2.3.3.1 Page 375 Groups in conduit Systems, cable trunking systems or cable ducting systems"""	
		self.Cg = 1/sqrt(self.n)
		return self.Cg
		
	def it_single_ccts(self):
		"""Clause 5.1.1 page 377 determination of the size of cable to be used for single circuits"""
		self.It = self.In/(self.Ca * self.Cs * self.Cd * self.Ci * self.Cf * self.Cc)
		return self.It
		
	def it_groups(self):
		"""Clause 5.1.2 page 378 determination of the size of cable to be used for groups of circuits"""
				
		self.Eq2 = self.In/(self.Cg * self.Ca * self.Cs * self.Cd * self.Ci * self.Cf * self.Cc)
		
		self.Eq3 = self.Ides/(self.Cg * self.Ca * self.Cs * self.Cd * self.Ci * self.Cf * self.Cc)

		self.Eq4 = (1/(self.Ca * self.Cs * self.Cd * self.Ci )) * (sqrt((self.In/(self.Cf * self.Cc))**2 + 0.48 * self.Ides**2 * ((1 - self.Cg**2)/self.Cg**2)) )
		
		# Which equation gives the highest result
		self.It = max(self.Eq2, self.Eq3, self.Eq4)
		return self.It
		
	def it_no_overload(self):
		"""Clause 5.2 Page 378 Where no overload protection is required"""
		self.It = self.Ides / (self.Cg * self.Ca * self.Cs * self.Cd * self.Ci * self.Cc)
		return self.It
		
	def ch(self):
		"""Clause 5.6 Page 381 Harmonic currents in line conductors"""
		self.Ch = sqrt((self.Ifun**2 + self.h3**2 + self.h5**2 + self.h7**2 + self.h9**2)/self.Ifun**2)
		return self.Ch
		
	def ct(self):
		"""Clause 6.1 Page 382 Correction for operating temperature"""
		
		self.Ct = (230 + self.Tp - (self.Ca**2 * self.Cg**2 * self.Cs**2 * self.Cd**2 - self.Ides**2 / self.It**2) * (self.Tp - 30)) / (230 + self.Tp)
				
		#Here I am checking for a negative Ct and if it finds it return a 1
		Ct = str(self.Ct)
		
		if Ct[0] =='-':
			self.Ct = 1
			return self.Ct
		else:
			return  self.Ct
	
	def mvam(self):
		"""Clause 6.2 Page 382 Correction for load power factor"""
		self.mVAmz = (cos(radians(self.Pf))*self.mVAmr) + (sin(radians(self.Pf))*self.mVAmx)
		return self.mVAmz
		
	def ctpf(self):
		""""Clause 6.3 Page 382 Correction for operating temperature and power factor"""
		
		Ct = self.Ct
		
		if self.mVAmx == 0:
			self.mVAmz = Ct * cos(radians(self.Pf)) * self.mVAmr
			return self.mVAmz
		else:
			self.mVAmz = Ct * cos(radians(self.Pf)) * self.mVAmr + sin(radians(self.Pf)) * self.mVAmx
			return self.mVAmz
		
#calling the class		

def main():
    my_cable = CableCalc(n=9, tp=70, ca=1, 
					cs=1, cd=1, ib=80, 
					it=300, ifun=10, h3=3, 
					h5=5, h7=2, h9=2, 
					ci = 1, cf = 1, cc =1, 
					inom = 100, pf = 0.8, 
					mvamr = 11, mvamx = 13)
    
    #printing out values for checking
    print("\nYour Cg factor is {}".format(str(my_cable.cg())))
    
    print("\nYour Ct Factor is {}".format(str(my_cable.ct())))
    
    print("\nYour Ch factor is {}".format(str(my_cable.ch())))
    
    print("\nYour single It should be equal or greater than {}".format(str(my_cable.it_single_ccts())))
    
    print("\nYour group It should be equal or greater than {}".format(str(my_cable.it_groups())))
    
    print("\nEquation 2 {}  Equation 3  {}  Equation 4  {}".format(str(my_cable.Eq2),str(my_cable.Eq3),str(my_cable.Eq4)))
    
    print("\nYour It where overload protection is not required {}".format(str(my_cable.it_no_overload())))
    
    print("\nYour mVAmz is  {}".format(str(my_cable.mvam())))
    
    print("\nYour CT * Pf * mV/A/m is  {}".format(str(my_cable.ctpf())))


if __name__ == '__main__': main()
    
    