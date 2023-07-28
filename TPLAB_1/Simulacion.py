# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:54:18 2023

@author: jron0
"""

import sympy as sp
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
from pytc2.sistemas_lineales import analyze_sys, tf2sos_analog, pretty_print_SOS, pretty_print_lti

plt.close('all')

w = 2*3.1416*6000
Q = 2.654

num= [w/Q, 0]
den= [1, w/Q, w*w]

#w0=1
#Q=2.654

tf_bp = sig.TransferFunction(num, den)
analyze_sys( tf_bp, 'BPF' )



