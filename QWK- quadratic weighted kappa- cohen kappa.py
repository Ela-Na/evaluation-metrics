# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:02:07 2020

@author: Ela
"""

from sklearn import metrics

y_true = [1, 2, 3, 1, 2, 3, 1, 2, 3]
y_pred = [2, 1, 3, 1, 2, 3, 3, 1, 2]

metrics.cohen_kappa_score(y_true, y_pred, weights="quadratic")

metrics.accuracy_score(y_true, y_pred)