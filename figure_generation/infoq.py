import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          ''')


F = np.linspace(0,1)
f = lambda x : np.sqrt(2*(1-np.sqrt(x)))

fig = plt.figure(1)
plt.plot(F,f(F), label = '')
plt.xlabel('$F$')
plt.ylabel('$\\norm{\\ket{\\psi_1} - \\ket{\\psi _2} }_2$')

fig.savefig('../figures/Fidelity.pdf', format = 'pdf')
