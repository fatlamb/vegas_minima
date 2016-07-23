#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys


from pylab import rcParams
rcParams['figure.figsize'] = 10, 8
plt.rc('font', size=16)


f=np.load("../output/fine_logwide_density_closetest_e6"+".npz")

kbar=f['kbar']
npoints=f['npoints']
nu=f['nu']

#print nu
#xedge=[0.09,2.1]
xedge=[0.01,10.0]

def nucut(nu,xlo,xhi):
	return xlo<=nu and nu <= xhi

nucut_vec = np.vectorize(nucut)
cut_indices=np.where(nucut_vec(nu,xedge[0],xedge[1]))


nu=f['nu'][cut_indices]

sigma=f['sigma']
kappa=f['kappa']


means=np.zeros((len(cut_indices[0]),len(kbar)))
sdevs=np.zeros((len(cut_indices[0]),len(kbar)))
pct_sdevs=np.zeros((len(cut_indices[0]),len(kbar)))


means=f['means'][cut_indices[0],:]
sdevs=f['sdevs'][cut_indices[0],:]
pct_sdevs=f['sdevs'][cut_indices[0],:]

print sigma


print means

axes=[]

colors=['red','orange','green','blue','purple']

axes.append(plt.subplot2grid((4,4),(0,0),colspan=4,rowspan=4))
for k in range(len(kbar)):

	print "KBAR: ",kbar[k], "  MAXPCT: ",np.max(pct_sdevs[:,k])

	axes[0].errorbar(nu,means[:,k],yerr=sdevs[:,k],marker="o",color=colors[k],linestyle='None',lw=1.0,label="Kbar: "+str(kbar[k]))
#axes[0].plot(xax_vector,pert_vec0,color="red",label="Standard Vacuum Solution",lw=2,ls='-')

#ax.set_ylim([1e-1,1])
#ax.set_ylim([0,1.0])
#axes[0].set_xlabel(r'$\nu$'+" (Field Standard Deviations)",fontsize=18)
axes[0].set_xlabel(r'$\nu$',fontsize=18)
axes[0].set_ylabel(r'$\langle \mathcal{N}_{min}(\nu) \rangle_{Q_2}$',fontsize=18)
axes[0].set_xlim(xedge)
axes[0].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))

axes[0].set_xscale('log')
"""
axes.append(plt.subplot2grid((4,4),(0,0),colspan=4,sharex=axes[0]))

#axes[1].plot(xax_vector,np.absolute(np.subtract(pert_vec1,num_vec)),color="green",lw=2,ls='--')
axes[1].errorbar(nu,errs_o,yerr=sdevs_o,linestyle='None',marker="^",color="blue",label="True Error Ordered")
axes[1].errorbar(nu,errs_uo,yerr=sdevs_uo,linestyle='None',marker="^",color="orange",label="True Error Un-Ordered")
axes[1].plot(truex,np.zeros(len(truex)),color="black")

#axes[1].set_title("Expectation Comparison: Analytic vs. Vegas")
axes[1].set_xlim(xedge)
axes[1].set_ylabel("Error")
#axes[1].set_ylim([0,100])
axes[1].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))
plt.setp(axes[1].get_xticklabels(), visible=False)
"""





# Now add the legend with some customizations.
#legend = ax.legend(loc='center right', shadow=False)
#legend = ax.legend(bbox_to_anchor=(0.9, 0.6), bbox_transform=plt.gcf().transFigure, shadow=False)

h1, l1 = axes[0].get_legend_handles_labels()
#h2, l2 = axes[1].get_legend_handles_labels()

#legend = axes[0].legend(h1+h2,l1+l2,bbox_to_anchor=(0.925, 0.4),shadow=False,fancybox=True)
#legend = axes[0].legend(h1+h2,l1+l2,loc='bottom right',shadow=False,fancybox=True)
legend = axes[0].legend(h1,l1,loc='upper right',shadow=False,fancybox=True)
#legend = axes[0].legend(h1+h2,l1+l2,bbox_to_anchor=(0.01, 0.7),bbox_transform=plt.gcf().transFigure, shadow=False,fancybox=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('1.0')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize(16)

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

for ax in axes:
	ax.tick_params(axis='x', which='major', labelsize=16)
	ax.tick_params(axis='y', which='major', labelsize=16)


# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='white', edgecolor='black')

"""
textlist=[
r'$\sigma_0=%.2f$'%(s0)+'\n',
r'$\sigma_1=%.2f$'%(s1)+'\n',
r'$\kappa=%.2f$'%(kap)]
textstr=''.join(textlist)

print textstr

#axes[0].text(0.415, 0.2375, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)
axes[0].text(0.025, 0.96, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)
"""
"""
props_o = dict(boxstyle='round', facecolor='blue', edgecolor='black',alpha=0.4)
props_uo = dict(boxstyle='round', facecolor='orange', edgecolor='black',alpha=0.4)
axes[0].text(0.3, 0.265, r'$\chi^2$'+'={:03.2f}'.format(chi2_o), transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props_o)
axes[0].text(0.3, 0.115, r'$\chi^2$'+'={:03.2f}'.format(chi2_uo), transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props_uo)

#visible_labels = [lab for lab in axes[0].get_yticklabels() if lab.get_visible() is True and lab.get_text() != '']
visible_labels = axes[1].get_yticklabels()
plt.setp(visible_labels[1::2], visible=False)
"""

plt.show()
#print sp.AtmosphericNeutrinoOscillationProbability(1,1,100*param.GeV,param.PI,param)

