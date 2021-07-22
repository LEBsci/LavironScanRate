import math, glob
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

#plt.style.use('bmh')
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rc('figure', figsize=(8,8))

def splot(PtN, cycle_per_scanrate, cycle_number): # The arguments are the miller index of the platinum electrode, the number of cycles done for each scan rate and the preferred cycle out of the total made
    pt = pd.read_csv('Pt' + str(PtN) + '.csv', header=None, skiprows=1, engine='python')
    lbls = ['10 mV/s', '20 mV/s', '50 mV/s', '75 mV/s', '100 mV/s', '200 mV/s'] # In this case, the number and selection of scan rates is written in the function. It could written in the data
    for n in range(0,len(pt.iloc[0,:])//cycle_per_scanrate):
        # plt.plot(pt.iloc[:,4*n], pt.iloc[:,4*n+1], label=lbls[n])
        plt.plot(pt.iloc[:,cycle_per_scanrate*n+cycle_number], pt.iloc[:,cycle_per_scanrate*n+cycle_number+1], label=lbls[n])
    plt.axhline(0, 0, 1, c = 'black')
    plt.xlabel('$E$/V vs Pd/H')
    plt.ylabel(r'$i\,/\,\mathrm{\mu A}$')
    plt.legend()
    plt.show()
    print(len(pt.iloc[0,:]))

splot(322, 4, 2)
