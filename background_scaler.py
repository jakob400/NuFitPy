def background_scaler(background_histvalues, file_histvalues):
    background_time = 548892
    #ratio = file_time / background_time
    #background_histvalues = background_histvalues * ratio
    file_histvalues = file_histvalues - background_histvalues
    file_histvalues = [abs(k) for k in file_histvalues] #returns nonnegative values for curve fitting

    return file_histvalues
