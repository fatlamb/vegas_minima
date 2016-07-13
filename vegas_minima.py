#! /usr/bin/python

import pyximport; pyximport.install()
import vegas
from minima_integrand import f_cython
import numpy as np

pi=np.pi
nu=1.0
s0=2.0
s1=2.0
kap=2.0

f = f_cython(dim=6,nu=nu,s0=s0,s1=s1,kap=kap)
integ = vegas.Integrator(6* [[-pi/2,pi/2]], nhcube_batch=1000)




fparallel = vegas.MPIintegrand(f)
integ(fparallel, nitn=10, neval=1000000)
result = integ(fparallel, nitn=10, neval=1000000)

if fparallel.rank==0:
	print result.summary()
	print 'result = %s    Q = %.2f' % (result, result.Q)
	truint = (-1.0)*(s1**6*(nu**4-6.0*nu**2+3.0))/(27.0*nu*s0**3)
	print truint

