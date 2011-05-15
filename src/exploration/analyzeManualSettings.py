# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:52:36 2011

@author: jan
"""

import scikits.audiolab as al
import matplotlib.pyplot as pl
import numpy as np
import analysistools as tools

wavs = [];
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M1_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M1.3_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M1.7_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M2_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M2.5_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M3.2_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M4_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M5_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M6.4_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M8_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M10_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M13_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M16_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M20_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M25_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M32_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M40_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M50_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M64_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M80_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M100_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M128_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
#wavs.append(al.wavread("Samples/Ch1_G1_M128_G2_M128_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G2_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_M128_G2_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G2_M32_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_M32_G2_M32_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G2_M1_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_M1_G2_M1_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_TTL-3.0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
#wavs.append(al.wavread("Samples/Ch1_G1_TTL-2.7_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_TTL_0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_TTL+3.0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_AA-3.0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
#wavs.append(al.wavread("Samples/Ch1_G1_AA_0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0])
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_AA+3.0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_TTL_0_G2_TTL_0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_TTL_0_G2_TTL_0_G3_TTL_0_NoMaster_NoFlashPresent_d7000.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M32_G2_TTL_0_G3_TTL_0_NoMaster_NoFlashPresent_sb900.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M32_G2_M32_G3_TTL_0_NoMaster_NoFlashPresent_sb900.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_M32_G2_TTL_0_G3_M32_NoMaster_NoFlashPresent_sb900.wav")[0][:,0]))
wavs.append(tools.normalize(al.wavread("Samples/Ch1_G1_TTL_0_G2_M32_G3_M32_NoMaster_NoFlashPresent_sb900.wav")[0][:,0]))
N = len(wavs);

# Extract the second chunk of every data block
chunks = [tools.findChunks(wav, 2500.0, 0.1) for wav in wavs]
bl2 = [wav[c[1].start:c[1].end] for (wav, c) in zip(wavs, chunks)]
td2 = [tools.findTdiffs(bl) for bl in bl2]
pl2 = [tools.findPulses(bl) for bl in bl2]
plnorm = [p - p[0] for p in pl2]

pl.plot(wavs[-1])
pl.show()

# Group pulses
corr = tools.groupPulses(plnorm)

# Plot result
pl.figure()
pl.hold(True)
for i in range(N):
    pl.plot(corr[i], i * np.ones(len(corr[i])), 'bx')
    
pl.show()