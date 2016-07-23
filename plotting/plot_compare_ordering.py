#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys

exponent = sys.argv[1]

def truint(mynu,mys0,mys1):
	return (-1.0)*(mys1**6*(mynu**4-6.0*mynu**2+3.0))/(27.0*mynu*mys0**3)


from pylab import rcParams
rcParams['figure.figsize'] = 10, 8
plt.rc('font', size=16)



f_o=np.load("../output/test_ordered_e"+str(exponent)+".npz")
f_uo=np.load("../output/test_unordered_e"+str(exponent)+".npz")

s0=f_o['s0']
s1=f_o['s1']
kap=f_o['kap']

npoints=f_o['npoints']

nu=f_o['nu']
#pct_sdevs=f['pct_sdevs']

#xedge=[0.09,2.1]
xedge=[0.1,2.05]

def nucut(nu,xlo,xhi):
	return xlo<=nu and nu <= xhi

nucut_vec = np.vectorize(nucut)

cut_indices=np.where(nucut_vec(nu,xedge[0],xedge[1]))
print cut_indices

nu=f_o['nu'][cut_indices]

sdevs_o=f_o['sdevs'][cut_indices]
means_o=f_o['means'][cut_indices]
errs_o=f_o['errs'][cut_indices]
pct_errs_o=f_o['pct_errs'][cut_indices]
abs_errs_o=f_o['abs_errs'][cut_indices]
sdevs_uo=f_uo['sdevs'][cut_indices]
means_uo=f_uo['means'][cut_indices]
errs_uo=f_uo['errs'][cut_indices]
pct_errs_uo=f_uo['pct_errs'][cut_indices]
abs_errs_uo=f_uo['abs_errs'][cut_indices]



truex_nsamp=1000
truex=np.linspace(xedge[0],xedge[1],1000)
truef_vec=np.vectorize(truint)
truey=truef_vec(truex,s0,s1)


axes=[]




axes.append(plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4))
axes[0].errorbar(nu,means_o,yerr=sdevs_o,marker="o",color='blue',linestyle='None',lw=1.0,label="Vegas Ordered: "+'{:02.0e}'.format(int(npoints)))
axes[0].errorbar(nu,means_uo,yerr=sdevs_uo,marker="o",color='orange',linestyle='None',lw=1.0,label="Vegas Un-Ordered: "+'{:02.0e}'.format(int(npoints)))
axes[0].plot(truex,truey,ls='-',lw=1.5,color='black',label="Analytic: Guth")
#axes[0].plot(xax_vector,pert_vec0,color="red",label="Standard Vacuum Solution",lw=2,ls='-')

#ax.set_yscale('log')
#ax.set_ylim([1e-1,1])
#ax.set_ylim([0,1.0])
axes[0].set_xlabel(r'$\nu$'+" (Field Standard Deviations)",fontsize=18)
axes[0].set_ylabel(r'$\langle \lambda_1 \lambda_2 \lambda_3 \rangle_{Q_2}$',fontsize=18)
axes[0].set_xlim(xedge)
axes[0].set_ylim([-10.0,3.0])
axes[0].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))

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






# Now add the legend with some customizations.
#legend = ax.legend(loc='center right', shadow=False)
#legend = ax.legend(bbox_to_anchor=(0.9, 0.6), bbox_transform=plt.gcf().transFigure, shadow=False)

h1, l1 = axes[0].get_legend_handles_labels()
h2, l2 = axes[1].get_legend_handles_labels()

#legend = axes[0].legend(h1+h2,l1+l2,bbox_to_anchor=(0.925, 0.4),shadow=False,fancybox=True)
legend = axes[0].legend(h1+h2,l1+l2,loc='bottom right',shadow=False,fancybox=True)
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




textlist=[
r'$\sigma_0=%.2f$'%(s0)+'\n',
r'$\sigma_1=%.2f$'%(s1)+'\n',
r'$\kappa=%.2f$'%(kap)]
textstr=''.join(textlist)

print textstr

#axes[0].text(0.415, 0.2375, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)
axes[0].text(0.025, 0.96, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)

"""
Calculate Chi2
"""

def chi2_el(mynu,mymean,mysig):
	return ((truint(mynu,s0,s1)-mymean)/mysig)**2

chi2_f=np.vectorize(chi2_el)

chi2_o=(1.0/float(len(nu)))*np.sum(chi2_f(nu,means_o,sdevs_o))
print "CHI2 Ordered: ",chi2_o
chi2_uo=(1.0/float(len(nu)))*np.sum(chi2_f(nu,means_uo,sdevs_uo))
print "CHI2 Un-Ordered: ",chi2_uo

print len(nu)

props_o = dict(boxstyle='round', facecolor='blue', edgecolor='black',alpha=0.4)
props_uo = dict(boxstyle='round', facecolor='orange', edgecolor='black',alpha=0.4)
axes[0].text(0.3, 0.265, r'$\chi^2$'+'={:03.2f}'.format(chi2_o), transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props_o)
axes[0].text(0.3, 0.115, r'$\chi^2$'+'={:03.2f}'.format(chi2_uo), transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props_uo)

#visible_labels = [lab for lab in axes[0].get_yticklabels() if lab.get_visible() is True and lab.get_text() != '']
visible_labels = axes[1].get_yticklabels()
plt.setp(visible_labels[1::2], visible=False)

plt.show()
#print sp.AtmosphericNeutrinoOscillationProbability(1,1,100*param.GeV,param.PI,param)

