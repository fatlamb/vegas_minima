#! /usr/bin/python

import pyximport; pyximport.install()
import vegas
import integrand as INT
import integrand_unordered as INTU
import numpy as np
#import time

def integrate(nu,s0,s1,kap,npoints,ordered=True,test=False):	
	pi=np.pi
	
	if ordered==True:
		f = INT.f_cython(dim=6,nu=nu,s0=s0,s1=s1,kap=kap)
		multiplicity_prefac=1.0
	if ordered==False:
		f = INTU.f_cython(dim=6,nu=nu,s0=s0,s1=s1,kap=kap)
		multiplicity_prefac=1.0/6.0

	if test==True:
		domain=[[-pi/2,pi/2],[-pi/2,pi/2],[-pi/2,pi/2],[-pi/2,pi/2],[-pi/2,pi/2],[-pi/2,pi/2]]
		density_prefac=1.0
	if test==False:
		domain=[[0,pi/2],[0,pi/2],[0,pi/2],[-pi/2,pi/2],[-pi/2,pi/2],[-pi/2,pi/2]]
		density_prefac= (3.0*np.sqrt(6.0)*nu*np.exp(-nu**2/2.0))/(4.0*np.pi**(3.0/2.0)*s1**3)
		
	integ = vegas.Integrator(domain, nhcube_batch=1000)
	
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

	
	retlist = [result.mean,result.sdev]
	for x in range(len(retlist)):
		retlist[x]*=density_prefac*multiplicity_prefac

	return retlist
