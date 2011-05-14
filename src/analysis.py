# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:41:46 2011

@author: jan
"""

import analysistools as at
import numpy as np
import pdb

def decodeInitialization(chunk, rate=96000.0):
    settings = {}
    diffs = at.findTdiffs(chunk) / (rate / 1000000.0)
    
    params = np.load("initialization_params.npz")
    
    # Decode channel
    # Calculate square error of received time distances with reference
    ch_times = diffs[0:2]
    dists = np.power(params['channels'] - ch_times, 2).sum(1)
    
    # TODO: Probably error message if minimum distance is too large
    
    # Assume the group with smallest error
    settings['channel'] = dists.argmin() + 1
    
    # Read intermediate, though not used here at the moment
    inter_dist = np.power(params['intermediate'] - diffs[2:5], 2).sum()
    
    # TODO: Probably error message if distance is too large
    
    # Read group settings
    settings['group'] = np.array([])
    pos = 5
    length = diffs.shape[0]
    
    while pos < (length - 1):
        if length - pos == 2:
            # Last presence pulse
            # Calculate distance, though not used here at the moment
            dist = np.power(params['grp_present'][0:2] - diffs[pos:pos+2], 2).sum()
            settings['group'] = np.append(settings['group'], True)
            pos += 2
        else:
            # There is more than one group remaining
            dist_present = np.power(params['grp_present'] - diffs[pos:pos+3], 2).sum()
            dist_absent = np.power(params['grp_absent'] - diffs[pos], 2)
            
            if dist_present < dist_absent:
                settings['group'] = np.append(settings['group'], True)
                pos += 3
            else:
                settings['group'] = np.append(settings['group'], False)
                pos += 1
    
    return settings
