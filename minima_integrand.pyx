#file: minima_integrand.pyx

cimport vegas
from libc.math cimport exp
from libc.math cimport sqrt
from libc.math cimport tan
from libc.math cimport cos

import vegas
import numpy

cdef class f_cython(vegas.BatchIntegrand):
	cdef double nu
	cdef double s0
	cdef double s1
	cdef double kap
	cdef double pi
	cdef double prefac
	cdef int dim

	def __init__(self,dim,nu,s0,s1,kap):
		self.dim=dim
		self.nu=nu
		self.s0=s0
		self.s1=s1
		self.kap=kap
		self.pi= 3.14159265358979323
		self.prefac = (30375.0*self.s0**6)/(16.0*sqrt(30.0)*self.pi**(5.0/2.0)*self.kap**5*self.s1**15*exp(-self.nu**2/2.0)*sqrt(self.kap**2-1.0))


	def __call__(self, double[:, ::1] x):
		cdef double[::1] f = numpy.empty(x.shape[0],float)
		cdef double[::1] tanx = numpy.empty(x.shape[1],float)
		cdef double ijac
		cdef int i,d
		for i in range(f.shape[0]):
			if(x[i,0]>=x[i,1] and x[i,1]>=x[i,2]):
				ijac=1.0
				for d in range(self.dim):
					ijac*=(1/cos(x[d]))**2
					tanx[d]=tan(x[i,d])

				f[i] = self.prefac*ijac*(tanx[0]-tanx[2])*(tanx[0]-tanx[1])*(tanx[1]-tanx[2])*(tanx[0]*tanx[1]*tanx[2])*np.etanxp((-1.0)*(0.5*nu**2 + (3.0/(2.0*s1**2))*(tanx[3]**2+tanx[4]**2+tanx[5]**2) + ((5.0*s0**2)/(4*kap**2*s1**4))*(3.0*(tanx[0]**2+tanx[1]**2+tanx[2]**2 - (2.0/(nu*s0))*(tanx[0]*tanx[3]**2 + tanx[1]*tanx[4]**2 + tanx[2]*tanx[5]**2) + (1.0/(nu**2*s0**2))*(tanx[3]**2+tanx[4]**2+tanx[5]**2)**2) - (tanx[0]+tanx[1]+tanx[2] - (1.0/(nu*s0))*(tanx[3]**2+tanx[4]**2+tanx[5]**2))**2) + (1.0/(2*s0**2*(kap**2-1)))*(nu*s0 + (s0**2/s1**2)*(tanx[0]+tanx[1]+tanx[2] - (1.0/(nu*s0))*(tanx[3]**2+tanx[4]**2+tanx[5]**2)))**2))  
			else:
				f[i]=0.0
		return f

