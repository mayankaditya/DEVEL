from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,AutoMinorLocator)
fs2=12

data=np.loadtxt("GRTAVG.DAT")
fig=plt.figure(figsize=(6,4))
ax1=fig.add_subplot(1,1,1)
ax1.plot(data[:,0],data[:,1],linewidth=1.5,label='Na-Na',zorder=2)
ax1.plot(data[:,0],data[:,2],linewidth=1.5,label='Na-P',zorder=2)
ax1.plot(data[:,0],data[:,3],linewidth=1.5,label='Na-S',zorder=2)
ax1.plot(data[:,0],data[:,4],linewidth=1.5,label='P-P',zorder=2)
ax1.plot(data[:,0],data[:,5],linewidth=1.5,label='P-S',zorder=2)
ax1.plot(data[:,0],data[:,6],linewidth=1.5,label='S-S',zorder=2)
ax1.set_xlim(1,7)
ax1.set_ylim(0,)
ax1.set_xlabel(r'r($\AA$)',fontsize=fs2)
ax1.set_ylabel(r'g(r)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)
plt.savefig("PDF.png",dpi=300,bbox_inches='tight')
plt.show()

