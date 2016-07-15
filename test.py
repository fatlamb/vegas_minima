#! /usr/bin/python

import numpy as np
import vegas_minima as vmin
from prettytable import PrettyTable
from tqdm import tqdm

"""
Define the true expectation value of lam1*lam2*lam3 without the heaviside
function in lam3, but with ordering in lambdas. This is to be used as
a verification that the vegas algorithm is performing well. Beacuse the integrand
is identical to the real case, but only the limits of integration change,
I expect good performance of vegas relative to this analytic form to be
a strong predictor of accuracy in the true estimates.
"""

def truint(mynu,mys0,mys1):
	return (-1.0)*(mys1**6*(mynu**4-6.0*mynu**2+3.0))/(27.0*mynu*mys0**3)


"""
Define parameters, as well as the set of values nu should loop over,
and the resolution.
"""

s0=2.0
s1=2.0
kap=2.0

nsamples=20
nu=np.linspace(1,2,nsamples)

npoints=1e6


"""
Initialize output vectors.
"""

means=np.zeros(nsamples)
sdevs=np.zeros(nsamples)

true_vals=np.zeros(nsamples)

pct_sdevs=np.zeros(nsamples)
abs_errs=np.zeros(nsamples)
pct_errs=np.zeros(nsamples)

"""
Run the vegas algorithm over varying nu.
"""

for samp in tqdm(range(nsamples)):
	ret = vmin.calculate_density(nu[samp],s0,s1,kap,npoints)
	means[samp]=ret[0]
	sdevs[samp]=ret[1]

	true_vals[samp]=truint(nu[samp],s0,s1)

	pct_sdevs[samp] = abs(100.0*(sdevs[samp])/means[samp])
	abs_errs[samp] = abs(means[samp]-true_vals[samp])
	pct_errs[samp] = abs(100.0*(means[samp]-true_vals[samp])/true_vals[samp])


"""
Format an output table for spot-checking!
"""

t = PrettyTable(['Nu','Means','True','Sdev','PctSdev','AbsErr','PctErr'])

for i in range(len(nu)):
	rowstrs=[]
	rowstrs.append('{:06.4f}'.format(nu[i]))
	rowstrs.append('{:06.4f}'.format(means[i]))
	rowstrs.append('{:06.4f}'.format(sdevs[i]))
	rowstrs.append('{:06.4f}'.format(true_vals[i]))
	rowstrs.append('{:06.4f}'.format(pct_sdevs[i]))
	rowstrs.append('{:06.4f}'.format(abs_errs[i]))
	rowstrs.append('{:06.4f}'.format(pct_errs[i]))
	t.add_row(rowstrs)

print t

"""
Write these arrays out to an npz file for plotting.
"""

np.savez("output/e6_pos_expectation_test.npz",npoints=npoints,s0=s0,s1=s1,kap=kap,nu=nu,means=means,sdevs=sdevs,true_vals=true_vals,pct_sdevs=pct_sdevs,abs_errs=abs_errs,pct_errs=pct_errs)


