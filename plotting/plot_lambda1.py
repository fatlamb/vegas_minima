#! /usr/bin/python
import matplotlib as mpl

import PhysConst as pc
import simple_propagate as sp
import numpy as np
import matplotlib.pyplot as plt
import PMNSGen
import SUGen
import random
import sys

import PerturbSolve
import O1Solve
import O2Solve

from pylab import rcParams
rcParams['figure.figsize'] = 10, 8
plt.rc('font',family='Times New Roman')
plt.rc('font', size=16)

param=pc.PhysicsConstants(1.0)


if (len(sys.argv)==1):
	numcomp=False
else:
	if (sys.argv[1]=="numcomp"):
		numcomp=True
	else:
		print "BAD INPUT"

data=np.load('lambda1_nomatter.npz')


phi=data['_phi']
theta=data['_theta']
l1=data['_l1']
l2=data['_l2']
E=data['_E']
potential=data['_potential']
valvec=data['_valvec']
num_vec=data['_num_vec']
diag_vec=data['_diag_vec']
frac_vec=data['_frac_vec']
O1_vec=data['_O1_vec']
O2_vec=data['_O2_vec']
pert_vec0=data['_pert_vec0']
pert_vec1=data['_pert_vec1']
pert_vec2=data['_pert_vec2']
delta=data['_delta']
ntype=data['_ntype']


pi=3.141592
#-----------------------------------------------------------------#
#Plotting data


axes=[]

xax_vector=valvec

axes.append(plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4))
axes[0].plot(xax_vector,pert_vec0,color="red",label="Standard Vacuum Solution",lw=2,ls='-')

axes[0].set_xlim([xax_vector[0],xax_vector[-1]])
#axes[0].set_xlim([5e-17,xax_vector[-1]])
axes[0].set_ylim([0.0,1.0])
axes[0].set_xlabel(r"$\lambda_1$ [TeV]")
axes[0].set_ylabel("Muon Neutrino Survival Fraction")
axes[0].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))

axes.append(plt.subplot2grid((4,4),(0,0),colspan=4,sharex=axes[0]))

axes[1].plot(xax_vector,np.absolute(np.subtract(pert_vec1,num_vec)),color="green",lw=2,ls='--')

axes[1].set_xlim([xax_vector[0],xax_vector[-1]])
#axes[1].set_xlim([5e-17,xax_vector[-1]])
axes[1].set_ylabel("Fractional Error")
#axes[1].set_ylim([-0.2,0.2])
axes[1].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))
plt.setp(axes[1].get_xticklabels(), visible=False)


legend=ax.legend((loc='lower left', shadow=False,fancybox=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame=legend.get_frame())
frame.set_facecolor('1.0')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize(16)

for label in legend.get_lines():
    label.set_linewidth(2.0)  # the legend line width

plt.show()

