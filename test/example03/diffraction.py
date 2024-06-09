from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,AutoMinorLocator)
fs2=12

data=np.loadtxt("HKL")
fig=plt.figure(figsize=(6,4))
ax1=fig.add_subplot(1,1,1)
ax1.plot(data[:,0],data[:,7],linewidth=1.5,label='Diffraction Peak ',zorder=2)
ax1.set_xlim(1,5)
ax1.set_ylim(0,)
ax1.set_xlabel(r'|Q|($\AA^{-1}$)',fontsize=fs2)
ax1.set_ylabel(r'Intensity (arb. unit)',fontsize=12)
ax1.legend(loc='upper right',fontsize=12,frameon=False)
plt.savefig("Diffraction.png",dpi=300,bbox_inches='tight')
plt.show()

