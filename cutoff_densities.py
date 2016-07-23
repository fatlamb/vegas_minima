#! /usr/bin/python

import numpy as np
import integrate
import scipy.integrate as scint
from prettytable import PrettyTable
from tqdm import tqdm

def calculate_sigmas(kbar):
	sigma=np.zeros(3)
	res=[]
	for n in range(0,3):
   		res.append( scint.quad(lambda x: x**(2.0*(float(n)+1.0))*(x**2/(5.0+x**5)),0.0,kbar))
		sigma[n] = (1.0/(2*np.pi**2))*res[n][0]

	kappa = (sigma[0]*sigma[2])/(sigma[1]**2)

	return kappa,sigma


"""
Define parameters, as well as the set of values nu should loop over,
and the resolution.
"""

kbar=np.linspace(2.0,6.0,5)
for k in kbar:
	kap,sig = calculate_sigmas(k)
	print k
	print kap
	print sig
	print


nsamples=100
nu=np.logspace(-2.0,1.0,nsamples)

npoints=1e6

"""
Initialize output vectors.
"""

means=np.zeros((nsamples,len(kbar)))
sdevs=np.zeros((nsamples,len(kbar)))
pct_sdevs=np.zeros((nsamples,len(kbar)))

"""
Run the vegas algorithm over varying nu.
"""

allsigmas=np.zeros((3,len(kbar)))
allkappas=np.zeros(len(kbar))

print kbar

for n in range(len(kbar)):

	kappa,sigma = calculate_sigmas(kbar[n])
	allsigmas[:,n] = sigma
	allkappas[n] = kappa 

	print
	print "Cutoff at k=",kbar[n]

	for samp in tqdm(range(nsamples)):
		ret = integrate.integrate(nu[samp],sigma[0],sigma[1],kappa,npoints,ordered=True,test=False)
		means[samp][n]=ret[0]
		sdevs[samp][n]=ret[1]
	
		pct_sdevs[samp][n] = abs(100.0*(sdevs[samp][n])/means[samp][n])


"""
Format an output table for spot-checking!
"""


for n in range(len(kbar)):
	print
	print "Cutoff at k=",kbar[n]
	t = PrettyTable(['Nu','Means','Sdev','PctSdev'])
	for i in range(len(nu)):
		rowstrs=[]
		rowstrs.append('{:06.4f}'.format(nu[i]))
		rowstrs.append('{:06.4f}'.format(means[i][n]))
		rowstrs.append('{:06.4f}'.format(sdevs[i][n]))
		rowstrs.append('{:06.4f}'.format(pct_sdevs[i][n]))
		t.add_row(rowstrs)
	
	print t



"""
Write these arrays out to an npz file for plotting.
"""

np.savez("output/fine_logwide_density_closetest_e6.npz",npoints=npoints,sigma=sigma,kappa=kappa,nu=nu,means=means,sdevs=sdevs,pct_sdevs=pct_sdevs,kbar=kbar)


