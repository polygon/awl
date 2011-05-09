# -*- coding: utf-8 -*-
"""
Created on Mon May  9 23:03:12 2011

@author: jan
"""

import scikits.audiolab as al
import matplotlib.pyplot as pl
import numpy as np
import analysistools as tools
import analysis as an

def annotateDist(x0, x1, y, text=None):
    #pl.arrow(x0, y, x1-x0, 0, hatch='|')
    pl.annotate('', xy=(x0, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='<->'))
    if text:
        pl.text(x0 + (x1 - x0) / 2.0, y+0.02, text, 
                horizontalalignment='center')

def plotRemoteSettings(chunk, rate=96000.0):
    # Decode remote settings
    settings = an.decodeRemoteSettings(chunk, rate)
    data = np.array(chunk)
    
    data = data / np.max(data)
    time = 1000000.0 * np.array(range(len(data))) / rate
    pl.figure()
    pl.plot(time, data)
    limits = pl.axis()
    pl.show()
    
data = al.wavread("Samples/Ch1_G1_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0]
c = tools.findChunks(data, 100, 0.1)
chunk = data[c[0].start:c[0].end]
plotRemoteSettings(chunk)