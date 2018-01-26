import csv    # import the csv package
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import norm
from scipy.optimize import curve_fit
from scipy.misc import factorial
from scipy import signal
import matplotlib.ticker as ticker
from background_scaler import background_scaler
from pprint import pprint
import pandas as pd
import math

from population_selection import population_selection






def plot(filetype, filename):
    pop = [] #I don't think this is used for anything.


    background_histvalues = np.genfromtxt('Data/bckgrnd2.dat', delimiter='', unpack = True, skip_header = 0 )



    while True:
        if ( filetype == '.csv' ):
                imported_data = np.genfromtxt(filename, delimiter=',', unpack = True, skip_header = 28 )  # Imports data file skipping first 28 lines
                histvalues = imported_data[2]
                break
        elif ( filetype == '.tsv' ):
                imported_data = np.genfromtxt(filename, delimiter='\t', unpack = True, skip_header = 23 )  # Imports data file skipping first 23 lines
                histvalues = imported_data[2]
                break
        elif ( filetype == '.dat' ):
                imported_data = np.genfromtxt(filename, delimiter='\n', unpack = True, skip_header = 0 )  # Imports data
                histvalues = imported_data.astype(int)
                break



    #f = pd.read_csv('runtimes.csv').as_matrix() #opening file
    #for i in range(len(f)):
        #print(filename[5:-4],'compared to ',f[i][0])
        #print(filename[5:-4])
        #print(f[i][0])
        #if (f[i][0] == filename[5:-4]): #checking if the file has a runtime in runtimes.csv
            #file_time = int(f[i][1]) # copying over sample runtime



    while True:
        yesno = input('\nWould you like to remove background noise?(y/n)\n')
        if all([yesno != 'y',yesno != 'n']):
            print('Invalid input')
        else:
            if yesno == 'y':
                histvalues = background_scaler(background_histvalues, histvalues ) #removing background noise
            break

    #while True:
    #    yesno = input('\nWould you like to normalize the data?(y/n)\n')
    #    if all([yesno != 'y',yesno != 'n']):
    #        print('Invalid input')
    #    else:
    #        if yesno == 'y':
    #            histvalues = np.array(histvalues)
    #            histvalues = ( histvalues / file_time ) #normalizing data
    #        break

    #^^^^^^^^This ruins breaks curve_fit for some reason



    while True:
        yesno = input('\nWould you like to preview the data? (y/n)\n')
        if all([yesno != 'y',yesno != 'n']):
            print('Invalid input')
        else:
            if yesno == 'y':
                binEdges = np.arange(len(histvalues))
                bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
                width = 1
                plt.bar(bincenters, histvalues[1:], width=width, color='b', yerr=0, label= 'Range Preview')
                plt.title('Record Your Range(s)', fontsize = 18)
                plt.show(block=False) #shows plot without blocking script
            break

    number_of_peaks = int(input('\nHow many peaks would you like to analyze \n'))
    analysis_range = [[None for i in range(2)] for j in range(number_of_peaks)]


    for i in range(number_of_peaks):
        print('\nPeak',int(i+1))
        analysis_range[i][0],analysis_range[i][1] = map(int, input('Enter a range "x1,x2": ').split(','))


    plt.close() #closes plot preview
    plt.clf() #clears plot preview
    print('\n')

    range_set = 0  #to start analysis at 0th peak
    for i in range(number_of_peaks): #iterates over peak ranges you established
        total_bins, throwaway = population_selection( histvalues, analysis_range, range_set )
        range_set = range_set + 1





    binEdges = np.arange(len(histvalues))
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    width = 1




    #plot the histogram as a bar chart with error bars (error bars are currently 0)
    plt.bar(bincenters, histvalues[1:], width=width, color='orange', yerr=0, label= '10sec')




    filename_to_save = filename[5:-4]
    plt.title('Plot of %s' % filename_to_save, fontsize = 18)   #set title on top of plot
    plt.xlabel('Channel', fontsize = 16)   #set x axis label
    plt.ylabel('Counts', fontsize = 16)




    plt.savefig( 'Plots/%s.png' % filename_to_save , bbox_inches = 'tight', dpi= 800 )
    plt.show()


    return
