#! /usr/bin/python

import numpy as np
import vegas

pi=np.pi

nu=1.0
s0=2.0
s1=2.0
kap=2.0
#def logl(x,nu,s0,s1,kap):

prefac = (30375.0*s0**6)/(16.0*np.sqrt(30.0)*pi**(5.0/2.0)*kap**5*s1**15*np.exp(-nu**2/2.0)*np.sqrt(kap**2-1.0))
print prefac

def integrand(arg):
		x=np.zeros(6)
		ijac=1.0
		for a in range(0,6):
			x[a]=np.tan(arg[a])
			ijac*=(1/np.cos(arg[a]))**2

		if(x[0]>=x[1] and x[1]>=x[2]):
			ret= (x[0]-x[2])*(x[0]-x[1])*(x[1]-x[2])*(x[0]*x[1]*x[2])*np.exp((-1.0)*(0.5*nu**2 + (3.0/(2.0*s1**2))*(x[3]**2+x[4]**2+x[5]**2) + ((5.0*s0**2)/(4*kap**2*s1**4))*(3.0*(x[0]**2+x[1]**2+x[2]**2 - (2.0/(nu*s0))*(x[0]*x[3]**2 + x[1]*x[4]**2 + x[2]*x[5]**2) + (1.0/(nu**2*s0**2))*(x[3]**2+x[4]**2+x[5]**2)**2) - (x[0]+x[1]+x[2] - (1.0/(nu*s0))*(x[3]**2+x[4]**2+x[5]**2))**2) + (1.0/(2*s0**2*(kap**2-1)))*(nu*s0 + (s0**2/s1**2)*(x[0]+x[1]+x[2] - (1.0/(nu*s0))*(x[3]**2+x[4]**2+x[5]**2)))**2))*prefac*ijac 
		else:
			ret=0.0
		return ret

print pi

integ=vegas.Integrator([[-pi/2.0,pi/2.0],[-pi/2.0,pi/2.0],[-pi/2.0,pi/2.0],[-pi/2.0,pi/2.0],[-pi/2.0,pi/2.0],[-pi/2.0,pi/2.0]])

integ(integrand,nitn=5,neval=100000)
result=integ(integrand,nitn=10,neval=100000)
print result.summary()
print 'result = %s    Q = %.2f' % (result, result.Q)



truint = (-1.0)*(s1**6*(nu**4-6.0*nu**2+3.0))/(27.0*nu*s0**3)
print truint

