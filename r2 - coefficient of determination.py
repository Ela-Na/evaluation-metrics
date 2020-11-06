# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:55:17 2020

@author: Ela
"""

import numpy as np

import math

def r2(y_true, y_pred):
    
    error = 0
    
    mean_y_true = np.mean(y_true)
    
    numerator = 0
    denominator = 0
    
    
    for yt, yp in zip(y_true, y_pred):
        
        numerator += (yt - yp) ** 2
        denominator += (yt - mean_y_true) ** 2
        
        r2_part = numerator / denominator
        
    
    return 1 - r2_part