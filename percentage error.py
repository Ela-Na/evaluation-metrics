# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:42:14 2020

@author: Ela
"""

def mean_percentage_error(y_true, y_pred):
    
    error = 0
    
    for yt, yp in zip(y_true, y_pred):
        
        error += (yt- yp / yt)
        
    return error / len(y_true)