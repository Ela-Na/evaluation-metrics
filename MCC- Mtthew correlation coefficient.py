# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:13:52 2020

@author: Ela
"""
def true_positive(y_true, y_pred):
    
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        
        if yt == 1 and yp == 1:
            tp += 1
            
    return tp


def true_negative(y_true, y_pred):
    
    tn = 0
    for yt, yp in zip(y_true, y_pred):
        
        if yt == 0 and yp == 0:
            tn += 1
            
    return tn


def false_positive(y_true, y_pred):
    
    fp = 0
    for yt, yp in zip(y_true, y_pred):
        
        if yt == 00 and yp == 1:
            fp += 1
            
    return fp

def false_negative(y_true, y_pred):
    
    fn = 0
    for yt, yp in zip(y_true, y_pred):
        
        if yt == 1 and yp == 0:
            fn += 1
            
    return fn



def mcc(yt, yp):
    
    tp = true_positive(yt, yp)
    tn = true_negative(yt, yp)
    fp = false_positive(yt, yp)
    fn = false_negative(yt, yp)
    
    
    numerator = (tp * tn) - (fp * fn)
    denominator = (
            (tp + fp) *
            (fn + tn) *
            (fp + tn) *
            (tp + fn))
    
    denominator = denominator ** 0.5
    
    return numerator / denominator