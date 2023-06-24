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

#num= [0.3766, 0]
#den= [1, 0.3766, 1]

w0=1
Q=2.654

num= [w0/Q, 0]
den= [1, w0/Q, w0^2]

tf_bp = sig.TransferFunction(num, den)

# Se plotea el pasabajos
analyze_sys( tf_bp, 'BPF' )


#pretty_print_SOS(tf_bp)

#pretty_print_SOS(tf_bp, mode='omegayq')



