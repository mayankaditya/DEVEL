from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,AutoMinorLocator)
fs2=12
fig=plt.figure(figsize=(12,12))




data=np.loadtxt("VANHOVE_PAIR_Na-Na")
ax1=fig.add_subplot(2,3,1)
time=(0,20,40,60,80)
for i in range(1,5): 
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,20)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'4$\pi$r$^2$G$_{distinct}$(Na-Na)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)




data=np.loadtxt("VANHOVE_PAIR_Na-P")
ax1=fig.add_subplot(2,3,2)
time=(0,20,40,60,80)
for i in range(1,5):
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,20)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'4$\pi$r$^2$G$_{distinct}$(Na-P)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)

data=np.loadtxt("VANHOVE_PAIR_Na-S")
ax1=fig.add_subplot(2,3,3)
time=(0,20,40,60,80)
for i in range(1,5):
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,20)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'4$\pi$r$^2$G$_{distinct}$(Na-S)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)

data=np.loadtxt("VANHOVE_PAIR_P-P")
ax1=fig.add_subplot(2,3,4)
time=(0,20,40,60,80)
for i in range(1,5):
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,20)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'4$\pi$r$^2$G$_{distinct}$(P-P)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)


data=np.loadtxt("VANHOVE_PAIR_P-S")
ax1=fig.add_subplot(2,3,5)
time=(0,20,40,60,80)
for i in range(1,5):
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,20)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'4$\pi$r$^2$G$_{distinct}$(P-S)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)

data=np.loadtxt("VANHOVE_PAIR_S-S")
ax1=fig.add_subplot(2,3,6)
time=(0,20,40,60,80)
for i in range(1,5):
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,20)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'4$\pi$r$^2$G$_{distinct}$(S-S)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)













plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.4)










plt.savefig("Van_Hove_Distinct.png",dpi=300,bbox_inches='tight')
plt.show()

