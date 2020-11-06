# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:33:50 2020

@author: Ela
"""

import numpy as np

import math

def mean_squared_log_error(y_true, y_pred):
    
    error = 0
    msle = 0
    rmsle = 0
    
    for yt, yp in zip(y_true, y_pred):
        
        error += (np.log(1 + yt ) - np.log(1 + yp)) ** 2
        
    msle = error / len(y_true)
    rmsle = math.sqrt(msle)
    
    return 'MSLE =' msle, 'RMSLE =' rmsle
