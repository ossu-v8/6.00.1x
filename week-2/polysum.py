# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:26:23 2019

@author: Nain
"""

import math

def polysum(n, s):
    
    area = (0.25*n*s**2) / math.tan(math.pi/n)
    perimeter = (n*s)**2
    
    return round(area + perimeter, 4)