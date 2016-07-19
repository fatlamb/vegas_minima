#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



def truint(mynu,mys0,mys1):
	return (-1.0)*(mys1**6*(mynu**4-6.0*mynu**2+3.0))/(27.0*mynu*mys0**3)


from pylab import rcParams
rcParams['figure.figsize'] = 10, 8
plt.rc('font', size=16)



f=np.load("../output/e3_pos_expectation_test.npz")

s0=f['s0']
s1=f['s1']
kap=f['kap']

npoints=f['npoints']

nu=f['nu']
sdevs=f['sdevs']
means=f['means']
pct_sdevs=f['pct_sdevs']
pct_errs=f['pct_errs']

xedge=[0.9,2.1]


truex_nsamp=1000
truex=np.linspace(xedge[0],xedge[1],1000)
truef_vec=np.vectorize(truint)
truey=truef_vec(truex,s0,s1)


axes=[]




axes.append(plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4))
axes[0].errorbar(nu,means,yerr=sdevs,marker="o",color='black',linestyle='None',lw=1.0,label="Vegas: "+'{:02.0e}'.format(int(npoints)))
axes[0].plot(truex,truey,ls='-',lw=1.5,color='red',label="Analytic: Guth")
#axes[0].plot(xax_vector,pert_vec0,color="red",label="Standard Vacuum Solution",lw=2,ls='-')

#ax.set_yscale('log')
#ax.set_ylim([1e-1,1])
#ax.set_ylim([0,1.0])
axes[0].set_xlabel(r'$\nu$'+" (Field Standard Deviations)",fontsize=18)
axes[0].set_ylabel(r'$\langle \lambda_1 \lambda_2 \lambda_3 \rangle_{Q_2}$',fontsize=18)
axes[0].set_xlim(xedge)
axes[0].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))

axes.append(plt.subplot2grid((4,4),(0,0),colspan=4,sharex=axes[0]))

#axes[1].plot(xax_vector,np.absolute(np.subtract(pert_vec1,num_vec)),color="green",lw=2,ls='--')
axes[1].plot(nu,pct_errs,linestyle='None',marker="o",color="blue",label="True Error")
axes[1].plot(nu,pct_sdevs,linestyle='None',marker="^",color="orange",label="Estimated Error: "+r'$\sigma/\mu$')

#axes[1].set_title("Expectation Comparison: Analytic vs. Vegas")
axes[1].set_xlim(xedge)
axes[1].set_ylabel("% Error")
#axes[1].set_ylim([0,100])
axes[1].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))
plt.setp(axes[1].get_xticklabels(), visible=False)






# Now add the legend with some customizations.
#legend = ax.legend(loc='center right', shadow=False)
#legend = ax.legend(bbox_to_anchor=(0.9, 0.6), bbox_transform=plt.gcf().transFigure, shadow=False)

h1, l1 = axes[0].get_legend_handles_labels()
h2, l2 = axes[1].get_legend_handles_labels()

legend = axes[0].legend(h1+h2,l1+l2,bbox_to_anchor=(0.925, 0.4),shadow=False,fancybox=True)
#legend = axes[0].legend(h1+h2,l1+l2,bbox_to_anchor=(0.01, 0.7),bbox_transform=plt.gcf().transFigure, shadow=False,fancybox=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('1.0')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize(16)

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

axes[0].tick_params(axis='x', which='major', labelsize=16)
axes[0].tick_params(axis='y', which='major', labelsize=16)


# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='white', edgecolor='black')




textlist=[
r'$\sigma_0=%.2f$'%(s0)+'\n',
r'$\sigma_1=%.2f$'%(s1)+'\n',
r'$\kappa=%.2f$'%(kap)]
textstr=''.join(textlist)

print textstr

#axes[0].text(0.415, 0.2375, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)
axes[0].text(0.035, 0.95, textstr, transform=axes[0].transAxes, fontsize=18,verticalalignment='top', bbox=props)

"""
Calculate Chi2
"""

def chi2_el(mynu,mymean,mysig):
	return ((truint(mynu,s0,s1)-mymean)/mysig)**2

chi2_f=np.vectorize(chi2_el)
chi2=(1.0/float(len(nu)))*np.sum(chi2_f(nu,means,sdevs))
print "CHI2: ",chi2

plt.show()
#print sp.AtmosphericNeutrinoOscillationProbability(1,1,100*param.GeV,param.PI,param)

