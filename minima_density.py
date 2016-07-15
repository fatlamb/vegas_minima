#! /usr/bin/python

import pyximport; pyximport.install()
import vegas
from minima_integrand import f_cython
import numpy as np
#import time

def calculate_density(nu,s0,s1,kap,npoints):	
	pi=np.pi
	
	f = f_cython(dim=6,nu=nu,s0=s0,s1=s1,kap=kap)
	integ = vegas.Integrator([[0,pi/2],[0,pi/2],[0,pi/2],[-pi/2,pi/2],[-pi/2,pi/2],[-pi/2,pi/2]], nhcube_batch=1000)
	
	#start = time.clock()
	
	integ(f, nitn=10, neval=npoints)
	result = integ(f, nitn=10, neval=npoints)
	
	#end = time.clock()
	"""	
	print result.summary()
	print 'result = %s    Q = %.2f' % (result, result.Q)
	truint = (-1.0)*(s1**6*(nu**4-6.0*nu**2+3.0))/(27.0*nu*s0**3)
	print truint
	print "TIME: ", end-start
	"""

	density_prefac= (3.0*np.sqrt(6.0)*nu*np.exp(-nu**2/2.0))/(4.0*np.pi**(3.0/2.0)*s1**3)
	
	return [result.mean*density_prefac,result.sdev*density_prefac]
