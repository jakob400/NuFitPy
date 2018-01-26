import numpy as np

def range_def( analysis_range, range_set ):

    analysis_start = analysis_range[range_set][0]
    analysis_end = analysis_range[range_set][1]
    analysis_bins = np.linspace(analysis_start, analysis_end , analysis_end - analysis_start) #defining range of analysis


    biggest_index = len(analysis_range) - 1
    total_start = analysis_range[0][0]
    total_end = analysis_range[biggest_index][1]
    total_bins = np.linspace(total_start, total_end, total_end - total_start)

    return analysis_bins, total_bins
