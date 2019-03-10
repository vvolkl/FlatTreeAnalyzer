import numpy as np
import matplotlib.pyplot as plt
import math

# evenly sampled time at 200ms intervals
pt = np.arange(5., 100., 1)

#_____________________________________________________________________________________________________
def f(pt):
    return 0.25*np.sqrt(2500./pt**2 + 25./pt + 1.)


# red dashes, blue squares and green triangles
plt.plot(pt, f(pt), lw=2.0, color='blue',  label='mu')
plt.plot(pt, 2*f(pt), lw=2.0, color='green', label='e, gamma')

plt.xlabel(r'$p_T [GeV]$', fontsize=18)
plt.ylabel(r'$\delta_\epsilon (\%)$', fontsize=18)

plt.legend()

#plt.show()
plt.savefig('delta_eff.eps',format='eps')
