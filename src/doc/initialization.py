# -*- coding: utf-8 -*-
"""
Created on Mon May  9 23:03:12 2011

@author: jan
"""

import scikits.audiolab as al
import matplotlib.pyplot as pl
from matplotlib import rc
import numpy as np
import analysistools as tools
import analysis as an

def annotateDist(x0, x1, y, text=None):
    #pl.arrow(x0, y, x1-x0, 0, hatch='|')
    pl.annotate('', xy=(x0, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='<->'))
    if text:
        pl.text(x0 + (x1 - x0) / 2.0, y+0.02, text, 
                horizontalalignment='center', fontsize=10)

def plotRemoteSettings(chunk, rate=96000.0):
    # Decode remote settings
    settings = an.decodeRemoteSettings(chunk, rate)
    data = np.array(chunk)
    pulses = 1000000.0 * tools.findPulses(chunk) / rate
    data = data / np.max(data)
    time = 1000000.0 * np.array(range(len(data))) / rate
    pl.figure()
    pl.plot(time, data)
    for i in range(len(pulses)-1):
        annotateDist(pulses[i], pulses[i+1], 1.0, '$%.1f\mu s$' % (pulses[i+1]-pulses[i]))
        
    annotateDist(pulses[0], pulses[2], 1.1, 'Channel %u' % settings['channel'])
    annotateDist(pulses[2], pulses[5], 1.1, 'Start group settings')
    
    pos = 5
    groups = settings['group']
    for i in range(len(groups)-1):
        if groups[i] == 0:
            annotateDist(pulses[pos], pulses[pos+1], 1.1, 'Group %c: Off' % chr(65 + i))
            pos += 1
        else:
            annotateDist(pulses[pos], pulses[pos+3], 1.1, 'Group %c: On' % chr(65 + i))
            pos += 3
            
    annotateDist(pulses[pos], pulses[pos+2], 1.1, 'Group %c: On (last)' % chr(65 + len(groups) - 1))
    
    limits = pl.axis()
    pl.axis([limits[0], limits[1], limits[2], 1.2])
    pl.xlabel('time / $\mu$s')
    pl.ylabel('Light intensity')
    pl.title('Example decoding of an initialization block')
    pl.show()
    
data = al.wavread("Samples/Ch1_G1_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0]
c = tools.findChunks(data, 100, 0.1)
chunk = data[c[0].start:c[0].end]
plotRemoteSettings(chunk)