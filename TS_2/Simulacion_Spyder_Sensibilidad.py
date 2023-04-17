#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Juan Ronchetti
"""

from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

plt.close('all')

R1 = 1000
R2 = 30000
R3 = 10000
C = 100e-6 

my_tf = TransferFunction( [-(R3/R1) * (1/ (C*C*R3*R3) )], [1, 1/(C*R2), (1/ (C*C*R3*R3) )] )


bodePlot(my_tf, fig_id=1 )

R_param = [ 0.1, 1, 10] # R=R1/R2

for R in range(len(R_param)):
    
    my_tf = TransferFunction( [1, -R], [1, 1] )
    
    bodePlot(my_tf, fig_id=1, filter_description = 'R={:3.3f}'.format(R_param[R]) )




