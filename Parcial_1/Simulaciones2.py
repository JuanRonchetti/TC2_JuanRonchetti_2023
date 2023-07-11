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
from pytc2.general import print_subtitle

plt.close('all')

# Pasabajos
num= [1, -1.41, 1]
den= [1,1.41,1]
tf_lp = sig.TransferFunction(num, den)
analyze_sys( tf_lp, 'LPF prototipo' )







