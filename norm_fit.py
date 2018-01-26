import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.optimize import curve_fit
from scipy.misc import factorial
from scipy import asarray as ar,exp
from math import sqrt


def poisson(k, mu,A):
    return A*(mu**k/factorial(k)) * np.exp(-mu)

def gaussian(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))


def norm_fit(bincenters, pop, range_set):
    nbins_int = np.arange(0,8600)
    pop = [x+1 for x in pop] #These lines do not affect the final plot visually. They simply add a value to each bin so that the curve_fit can function properly.

    to_subtract = 0
    #change bincenters to make poisson-calculable
    if bincenters[0] > 1: #only if you have big bincenters values
        to_subtract = bincenters[0]
        bincenters = [ x - to_subtract for x in bincenters ]

    pop = np.array(pop) #because curve_fit expects this type
    bincenters = np.array(bincenters)

    peak1y =[]
    errpeak1y=[]
    peak1x =range(len(bincenters))
    for x in peak1x:
        peak1y.append(pop[x])
        errpeak1y.append(sqrt(pop[x]))

    #plt.errorbar(peak1x + to_subtract, peak1y,errpeak1y,fmt='o')
    #plotting error bars

    counts_taken_in_range = sum(pop)


    # fit with curve_fit
    parameters, cov_matrix = curve_fit(gaussian, peak1x, peak1y)
    print ('Amplitude = %.5f \t Mean = %.5f \t Sigma = %.5f \t Counts = %.5f' % (parameters[0],parameters[1]+to_subtract,parameters[2], counts_taken_in_range) )


    #if (os.path.exists('sample_output.csv')):
        #df = pd.read_csv("sample_output.csv", index_col=0,encoding='latin-1')
        #d = df.to_dict("split")
        #d = dict(zip(d["index"], d["data"]))
        #df = pd.DataFrame.from_dict(parameters, orient="index")
        #df.to_csv("data.csv")

    #Now lets plot a poisson distribution
    plt.plot(nbins_int, gaussian(nbins_int-to_subtract, *parameters),'green', lw=2)#plots after shifting back x values
    #plt.text(4000, 250 + 20*range_set,'mean = %.2f  sigma = %.2f' % (parameters[1]+to_subtract,parameters[2]),fontsize=14,)
    #plt.plot(nbins_int, gaussian(nbins_int, *parameters),'green', lw=2)
    #plt.text(500,500,'Amplitude = %.5f \t Mean = %.5f \n Sigma = %.5f \t Counts = %.5f' % (parameters[0],parameters[1]+to_subtract,parameters[2], counts_taken_in_range))
