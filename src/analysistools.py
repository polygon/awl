# -*- coding: utf-8 -*-
"""
Created on Sun May  1 01:35:37 2011

@author: jan
"""

import pdb
import numpy as np

class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
        
    def __str__(self):
        return self.__dict__.__str__()

def findChunks(data, offtime, threshold):
    state = 0
    ch_start = 0
    ch_end = 0
    pos = 0
    chunks = []
    below = 0

    for pos, val in enumerate(data):
        # Currently looking for the start of a chunk
        if state == 0:
            if val > threshold: # Found a chunk
                ch_start = pos
                ch_end = pos
                state = 1
                below = 0
                
        # Currently looking for the end of a chunk
        else:
            if val > threshold: # Update chunk end
                below = 0             # Reset below counter
                ch_end = pos
            else:
                below = below + 1
                if below >= offtime: # Chunk ends
                    chunks.append(Bunch(start=ch_start, end=ch_end, \
                                        length=ch_end-ch_start))
                    state = 0
                    
    if state == 1:
        chunks.append(Bunch(start=ch_start, end=ch_end, \
                            length=ch_end-ch_start))
    return chunks

def findTdiffs(data, offtime=2, threshold=0.7):
    peaks = findChunks(data, offtime, threshold)
    tdiffs = [];
    for i in range(1, len(peaks)):
        tdiffs.append((peaks[i].start + (peaks[i].end - peaks[i].start) / 2.0) - \
                      (peaks[i-1].start + (peaks[i-1].end - peaks[i-1].start) / 2.0))
    return np.array(tdiffs)
    
def findPulses(data, offtime=2, threshold=0.7):
    peaks = findChunks(data, offtime, threshold)
    pulses = [(p.start + p.end) / 2.0 for p in peaks]
    return np.array(pulses)

def diffSig( s1, s2 ):
# Will pad the shorter signal with zeros and gives
# The difference between the signals

    diff = np.zeros(np.max(len(s1), len(s2)))
    if len(s1) < len(s2):
        diff[0:len(s1)] = s2[0:len(s1)] - s1;
        diff = abs(diff)
    else:
        diff[0:len(s1)] = s1[0:len(s2)] - s2;
        diff = abs(diff)
        
    return diff
    
def groupPulses(pulses, tol=10):
    # Generate the data bins
    bins = []
    
    for pg in pulses:
        for pulse in pg:
            if not bins: # First bin
                bins.append(Bunch(pos=pulse,entries=[pulse]))
            else:
                binidx = np.nonzero(np.abs(np.array([b.pos for b in bins]) \
                                    - pulse) < tol)[0]
                if not len(binidx):
                    bins.append(Bunch(pos=pulse,entries=[pulse]))
                else:
                    bins[binidx[0]].entries.append(pulse)
                    
    # Generate average bin positions
    for b in bins:
        b.average = np.mean(b.entries)
        
    # Assign pulses to bins
    binpos = np.array([b.pos for b in bins])
    grouped = [np.zeros(len(p)) for p in pulses]
    
    for i, pg in enumerate(pulses):
        for j, pulse in enumerate(pg):
            # Find output pit
            grouped[i][j] = bins[np.argmin(np.abs(binpos - pulse))].average
            
    return grouped
    

#  % Generate output pulse positions
#  posout = posin;
#  for i=1:N
#    for j=1:length(posin{i});
#      % Find output pit
#      for k=1:length(pits)
#        if abs(pits(k).pos - posin{i}(j)) < tol
#          posout{i}(j) = pits(k).avgpos;
#          break;
#        end
#      end
#    end
#  end
