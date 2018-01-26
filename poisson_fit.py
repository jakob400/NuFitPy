import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.optimize import curve_fit
from scipy.misc import factorial


def poisson(k, mu,A):
    return A*(mu**k/factorial(k)) * np.exp(-mu)



def poisson_fit(bincenters, pop):
    nbins_int = np.arange(0,1000)
    pop = [x+1 for x in pop] #These lines do not affect the final plot visually. They simply add a value to each bin so that the curve_fit can function properly.

    to_subtract = 0
    #change bincenters to make poisson-calculable
    if bincenters[0] > 1: #only if you have big bincenters values
        to_subtract = bincenters[0]
        bincenters = [ x - to_subtract for x in bincenters ]

    pop = np.array(pop) #because poisson expects this type
    bincenters = np.array(bincenters)

    # fit with curve_fit
    parameters, cov_matrix = curve_fit(poisson, bincenters, pop)
    print (parameters[0]+to_subtract,parameters[1])
    #Now lets plot a poisson distribution
    plt.plot(nbins_int, poisson(nbins_int-to_subtract, *parameters),'green', lw=2)#plots after shifting back x values
