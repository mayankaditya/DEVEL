from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,AutoMinorLocator)
fs2=12

data=np.loadtxt("ANGLEVAR.DAT")
fig=plt.figure(figsize=(6,4))
ax1=fig.add_subplot(1,1,1)
ax1.plot(data[:,0],data[:,1],linewidth=1.5,label='P-S Angle in PS4 ',zorder=2)
ax1.plot(data[:,0],data[:,2],linewidth=1.5,label='Na-S Angle NaS6',zorder=2)
ax1.set_xlim(0,180)
ax1.set_ylim(0,)
ax1.set_xlabel(r'angle($\theta$)',fontsize=fs2)
ax1.set_ylabel(r'Intensity (arb. unit)',fontsize=12)
ax1.legend(loc='upper left',fontsize=12,frameon=False)
plt.savefig("Angle.png",dpi=300,bbox_inches='tight')
plt.show()

