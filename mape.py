# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:45:11 2020

@author: Ela
"""

import numpy as np

import math

def mean_abs_percentage_error(y_true, y_pred):
    
    error = 0
    
    
    for yt, yp in zip(y_true, y_pred):
        
        error += (np.abs(yt - yp) / yt
        
    
    return error / len(y_true)
