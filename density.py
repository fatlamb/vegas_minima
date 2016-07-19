#! /usr/bin/python

import numpy as np
import integrate 
from prettytable import PrettyTable
from tqdm import tqdm


"""
Define parameters, as well as the set of values nu should loop over,
and the resolution.
"""

s0=2.0
s1=2.0
kap=2.0

nsamples=10

neg=np.linspace(-7.5,0,nsamples/2,False)
pos=np.multiply(-1.0,neg)[::-1]
nu=np.concatenate((neg,pos))

npoints=1e6


"""
Initialize output vectors.
"""

means=np.zeros(nsamples)
sdevs=np.zeros(nsamples)

pct_sdevs=np.zeros(nsamples)


"""
Run the vegas algorithm over varying nu.
"""

for samp in tqdm(range(nsamples)):
	ret = integrate.integrate(nu[samp],s0,s1,kap,npoints,ordered=True,test=False)
	means[samp]=ret[0]
	sdevs[samp]=ret[1]

	pct_sdevs[samp] = abs(100.0*(sdevs[samp])/means[samp])


"""
Format an output table for spot-checking!
"""

t = PrettyTable(['Nu','Means','Sdev','PctSdev'])

for i in range(len(nu)):
	rowstrs=[]
	rowstrs.append('{:06.4f}'.format(nu[i]))
	rowstrs.append('{:06.4f}'.format(means[i]))
	rowstrs.append('{:06.4f}'.format(sdevs[i]))
	rowstrs.append('{:06.4f}'.format(pct_sdevs[i]))

	t.add_row(rowstrs)

print t

"""
Write these arrays out to an npz file for plotting.
"""

np.savez("output/ordered_e6_density.npz",npoints=npoints,s0=s0,s1=s1,kap=kap,nu=nu,means=means,sdevs=sdevs,pct_sdevs=pct_sdevs)


