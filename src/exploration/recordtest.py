# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:02:07 2011

@author: jan
"""

import pyaudio
import matplotlib.pyplot as pl
import numpy as np
import analysistools as tools
import struct

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=96000,
                input=True,
                frames_per_buffer=1024)
         
for i in range(30):
    stream.read(1024)         
         
ct = 468
data = []
for i in range(ct):
    buf = stream.read(1024)
    for j in range(len(buf)/4):
        data.append(struct.unpack('f', buf[(4*j):(4*j+4)])[0])
        
stream.close()
p.terminate()
data2 = np.array(data)
pl.plot(data)