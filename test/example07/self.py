from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,AutoMinorLocator)
fs2=12
fig=plt.figure(figsize=(12,4))

data=np.loadtxt("VANHOVE_SELF01")
ax1=fig.add_subplot(1,3,1)
#ax1.set_titel('Na')
time=(0,20,40,60,80)
for i in range(1,5): 
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,0.005)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'G$_{self}$(Na)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)

data=np.loadtxt("VANHOVE_SELF02")
ax1=fig.add_subplot(1,3,2)
#ax1.set_titel('Na')
time=(0,20,40,60,80)
for i in range(1,5):
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,0.02)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'G$_{self}$(P)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)


data=np.loadtxt("VANHOVE_SELF03")
ax1=fig.add_subplot(1,3,3)
#ax1.set_titel('Na')
time=(0,20,40,60,80)
for i in range(1,5):
 ax1.plot(data[:,0],data[:,i],linewidth=1.5,label=str(time[i-1])+' ps',zorder=2)
ax1.set_xlim(0,10)
ax1.set_ylim(0,0.02)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'G$_{self}$(S)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.4)










plt.savefig("Van_Hove_Self.png",dpi=300,bbox_inches='tight')
plt.show()

