#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


from pylab import rcParams
rcParams['figure.figsize'] = 10, 8
plt.rc('font', size=16)



f=np.load("../output/fine_e6_density.npz")

s0=f['s0']
s1=f['s1']
kap=f['kap']

npoints=f['npoints']

nu=f['nu']
sdevs=f['sdevs']
means=f['means']


fig,ax=plt.subplots()       

ax.errorbar(nu,means,yerr=sdevs,fmt="o",label="Vegas: "+'{:02.0e}'.format(int(npoints)))

#ax.set_yscale('log')
#ax.set_ylim([1e-1,1])
#ax.set_ylim([0,1.0])
#ax.set_xlim([0,1.65e4])
ax.set_xlabel(r'$\nu$'+" (Field Standard Deviations)",fontsize=18)
ax.set_ylabel(r'$\langle \mathcal{N}_{min}(\nu) \rangle_{Q_2}$',fontsize=18)
#ax.set_title("Expectation Comparison: Analytic vs. Vegas")


# Now add the legend with some customizations.
#legend = ax.legend(loc='center right', shadow=False)
#legend = ax.legend(bbox_to_anchor=(0.9, 0.6), bbox_transform=plt.gcf().transFigure, shadow=False)
legend = ax.legend(loc='upper right', shadow=False,fancybox=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('1.0')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize(16)

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

ax.tick_params(axis='x', which='major', labelsize=16)
ax.tick_params(axis='y', which='major', labelsize=16)

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='white', edgecolor='black')




textlist=[
r'$\sigma_0=%.2f$'%(s0)+'\n',
r'$\sigma_1=%.2f$'%(s1)+'\n',
r'$\kappa=%.2f$'%(kap)]
textstr=''.join(textlist)

print textstr

ax.text(0.03, 0.175, textstr, transform=ax.transAxes, fontsize=18,verticalalignment='top', bbox=props)



plt.show()
#print sp.AtmosphericNeutrinoOscillationProbability(1,1,100*param.GeV,param.PI,param)

