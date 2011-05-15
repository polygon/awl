# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:25:02 2011

@author: Jan Dohl

"""

import scikits.audiolab as al
import matplotlib.pyplot as pl
from numpy import *
import analysistools as tools

wavs = [];
wavs.append(al.wavread("Samples/Ch1_G1_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
wavs.append(al.wavread("Samples/Ch1_G2_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
wavs.append(al.wavread("Samples/Ch1_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
wavs.append(al.wavread("Samples/Ch1_G1_M128_G2_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
wavs.append(al.wavread("Samples/Ch1_G1_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
wavs.append(al.wavread("Samples/Ch1_G2_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
wavs.append(al.wavread("Samples/Ch1_G1_M128_G2_M128_G3_M128_NoMaster_NoFlashPresent_sb900.wav")[0][:,0])
N = len(wavs)

chunks = [];
bl1 = [];
td1 = [];
for wav in wavs:
    nc = tools.findChunks(wav, 1000.0, 0.1)
    chunks.append(nc)
    bl1.append(wav[nc[0].start:nc[0].end]);
    td1.append(tools.findTdiffs(bl1[-1]));
    
# Calculate average tdiffs for the next three blocks
tdb1 = 0.0
tdb2 = 0.0
tdb3 = 0.0
for td in td1:
    tdb1 = tdb1 + td[2]
    tdb2 = tdb2 + td[3]
    tdb3 = tdb3 + td[4]

tdb1 = (tdb1 / N);
tdb2 = (tdb2 / N);
tdb3 = (tdb3 / N);

# Calculate average tdiffs for Group Present pulse information
tgp1 = td1[0][5] + \
       td1[1][6] + \
       td1[2][7] + \
       td1[3][5] + td1[3][8] + \
       td1[4][5] + td1[4][9] + \
       td1[5][6] + td1[5][9] + \
       td1[6][5] + td1[6][8] + td1[6][11]
     
tgp2 = td1[0][6] + \
       td1[1][7] + \
       td1[2][8] + \
       td1[3][6] + td1[3][9] + \
       td1[4][6] + td1[4][10] + \
       td1[5][7] + td1[5][10] + \
       td1[6][6] + td1[6][9] + td1[6][12]
  
tgp3 = td1[3][7] + \
       td1[4][7] + \
       td1[5][8] + \
       td1[6][7] + td1[6][10]
     
tgp1 = (tgp1 / 12.0)
tgp2 = (tgp2 / 12.0)
tgp3 = (tgp3 / 5.0)

# Calculate average tdiffs for Group Absent pulse information
tga = td1[1][5] + \
      td1[2][5] + td1[2][6] + \
      td1[4][8] + \
      td1[5][5]
      
tga = ((tga / 5.0) / 96000.0) * 1000000.0

pl.figure()
pl.hold(True)

for bl in bl1:
    pl.plot(bl)

pl.show()