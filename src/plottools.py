# -*- coding: utf-8 -*-
"""
Created on Sun May  1 12:14:07 2011

@author: jan
"""

import numpy as np
import matplotlib.pyplot as pl
import analysistools as at
import pdb

def plotChunks(data, chunks=None):
    # Plots given chunks over the data
    # If no chunks are given, will search for chunks
    
    if chunks == None:
        chunks = at.findChunks(data, 1000.0, 0.3)

    csig = np.zeros(chunks[-1].end)
    for chunk in chunks:
        csig[chunk.start:chunk.end] = 1
        
    pdb.set_trace()
    pl.figure()
    pl.plot(data)
    pl.hold(True)
    pl.plot(csig, "r-")
    pl.show()

def plotClock(chunk, freq, offset):
    pl.figure()
    pl.plot(chunk)
    pl.hold(True)
    pos = offset
    while pos < len(chunk):
        pl.plot(np.round(pos) * np.array([1.0, 1.0]), \
                np.array([0, 1.3]), 'r-')
        pos = pos + freq
    pl.show()

#function plotClock( chunk, freq, offset )
#  hold off;
#  plot(chunk);
#  hold on;
#  pos = offset;
#  while pos < length(chunk);
#    plot([round(pos) round(pos)], [0, 1.3], 'r-');
#    pos = pos + freq;
#  end
#end