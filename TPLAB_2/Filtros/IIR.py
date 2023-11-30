#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:47:31 2023

@author: alumno
"""
import numpy as np
import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys, plot_plantilla
import matplotlib.pyplot as plt

fs = 1000
nyq = fs/2

wp = np.array([3, 25]) / nyq
ws = np.array([1, 35]) / nyq 
gpass = 0.1
gstop = 40

#plot_plantilla(filter_type = 'bandpass', fpass = wp*nyq, ripple = gpass , fstop = ws*nyq, attenuation = gstop)
               
num, den = sos = sig.iirdesign(wp, ws, gpass, gstop, analog=False,ftype='butter', output='ba')
sos = sig.iirdesign(wp, ws, gpass, gstop, analog=False,ftype='butter', output='SOS')

wrad, hh = sig.sosfreqz(sos, worN=1000)
ww = wrad/np.pi * (fs/2)

wrad2, hh2 = sig.freqz(num, den, worN=1000)
ww2 = wrad2/np.pi * (fs/2)

plt.plot(ww, 20 * np.log10(abs(hh)), label='IIR por SOS')
plt.plot(ww2, 20 * np.log10(abs(hh2)), label='IIR por ba')
plt.title('Filtro')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.grid()
plt.axis([0, 300, -600, 5 ]);


