import numpy as np

from poisson_fit import poisson_fit
from norm_fit import norm_fit
from range_def import range_def

def population_selection ( histvalues, analysis_range, range_set ):
    analysis_bins, total_bins = range_def( analysis_range, range_set ) #establishing range parameters


    #pop,binEdges = np.histogram(histvalues,analysis_bins) #pop is selection from histvalues based on analysis_bins
    binEdges = analysis_bins

    biggest_index = len(analysis_range) - 1
    lower_bound = analysis_range[range_set][0] #highest range for given analysis
    upper_bound = analysis_range[range_set][1]
    max_bound = analysis_range[biggest_index][1] #highest total bound

    pop = histvalues[lower_bound+1:upper_bound]

    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    width = 0.5
    norm_fit ( bincenters, pop ,range_set ) #fitting curve, and plotting fit

    histvalues = histvalues[lower_bound+1:max_bound]

    return total_bins, histvalues
