# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:41:46 2011

@author: jan
"""

import analysistools as at
import numpy as np
import pdb

def decodeRemoteSettings(chunk, rate=96000.0):
    settings = {}
    diffs = at.findTdiffs(chunk) / (rate / 1000000.0)
    
    params = np.load("remote_settings_params.npz")
    
    # Decode channel
    # Calculate square error of received time distances with reference
    ch_times = diffs[0:2]
    dists = np.power(params['channels'] - ch_times, 2).sum(1)
    
    # TODO: Probably error message if minimum distance is too large
    
    # Assume the group with smallest error
    settings['group'] = dists.argmin() + 1
    
    return settings