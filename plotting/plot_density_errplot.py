#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl




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
pct_sdevs=f['pct_sdevs']


axes=[]

axes.append(plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4))
axes[0].errorbar(nu,means,yerr=sdevs,marker="o",color='black',linestyle='None',lw=1.0,label="Vegas: "+'{:02.0e}'.format(int(npoints)))

#ax.set_yscale('log')
#ax.set_ylim([1e-1,1])
#ax.set_ylim([0,1.0])
axes[0].set_xlabel(r'$\nu$'+" (Field Standard Deviations)",fontsize=18)
axes[0].set_ylabel(r'$\langle \mathcal{N}_{min}(\nu) \rangle_{Q_2}$',fontsize=18)
axes[0].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))

axes.append(plt.subplot2grid((4,4),(0,0),colspan=4,sharex=axes[0]))

#axes[1].plot(xax_vector,np.absolute(np.subtract(pert_vec1,num_vec)),color="green",lw=2,ls='--')
axes[1].plot(nu,pct_sdevs,linestyle='None',marker="^",color="blue",label="Estimated Error: "+r'$\sigma/\mu$')

#axes[1].set_title("Expectation Comparison: Analytic vs. Vegas")
axes[1].set_ylabel("% Error")
#axes[1].set_ylim([0,100])
axes[1].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))
plt.setp(axes[1].get_xticklabels(), visible=False)






# Now add the legend with some customizations.
#legend = ax.legend(loc='center right', shadow=False)
#legend = ax.legend(bbox_to_anchor=(0.9, 0.6), bbox_transform=plt.gcf().transFigure, shadow=False)

h1, l1 = axes[0].get_legend_handles_labels()
h2, l2 = axes[1].get_legend_handles_labels()

#legend = axes[0].legend(h1+h2,l1+l2,bbox_to_anchor=(0.925, 0.4),shadow=False,fancybox=True)
legend = axes[0].legend(h1+h2,l1+l2,loc='lower right',shadow=False,fancybox=True)
#legend = axes[0].legend(h1+h2,l1+l2,bbox_to_anchor=(0.01, 0.7),bbox_transform=plt.gcf().transFigure, shadow=False,fancybox=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('1.0')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize(16)

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

axes[1].tick_params(axis='x', which='major', labelsize=14)
axes[1].tick_params(axis='y', which='major', labelsize=12)
axes[0].tick_params(axis='x', which='major', labelsize=14)
axes[0].tick_params(axis='y', which='major', labelsize=14)


# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='white', edgecolor='black')




textlist=[
r'$\sigma_0=%.2f$'%(s0)+'\n',
r'$\sigma_1=%.2f$'%(s1)+'\n',
r'$\kappa=%.2f$'%(kap)]
textstr=''.join(textlist)

print textstr

#axes[0].text(0.415, 0.2375, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)
axes[0].text(0.03, 0.95, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)

plt.show()
#print sp.AtmosphericNeutrinoOscillationProbability(1,1,100*param.GeV,param.PI,param)

