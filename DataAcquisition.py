# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 01:33:05 2022

@author: Shubhi Kant
"""

#%% Importing Dependencies
import os
import ftplib

#%% Downloading Jason-2 IGDR Products
"""
Jason 2 IGDR data has to be downloaded for cyles 092 to 203 corresponding to a 
time period of 3 years between 2011-2014.
"""
os.chdir(r'C:\Users\Omen\OneDrive\Desktop\Coastal_Altimetry\Coastal_data\j2_igdr')

FTP_HOST = "ftp-oceans.ncei.noaa.gov"
# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, 'anonymous', '')
# force UTF-8 encoding
ftp.encoding = "utf-8"

ftp.cwd('/pub/data.nodc/jason2/igdr/s_igdr/')

for i in range(92,203):
    if i < 100:
        files = ftp.nlst('cycle0'+str(i))
    else:
        files = ftp.nlst('cycle'+str(i))
    for f in files:
        if f[26:28] == '52':
            with open(f[9:]+'.nc', "wb") as file:
                ftp.retrbinary(f"RETR {f}", file.write)
            break
    print(f'cycle {i}: completed')

#%% Downloading PISTACH data
FTP_HOST = "ftp-access.aviso.altimetry.fr"
FTP_USER = "shubhka@iitk.ac.in"
FTP_PASS = "xB8QkH"

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"

os.chdir(r'C:\Users\Omen\OneDrive\Desktop\Coastal_Altimetry\Coastal_data\j2_pistach')

ftp.cwd('pub/oceano/pistach/J2/IGDR/coastal')

for i in range(92,203):
    if i < 100:
        ftp.cwd('cycle_0'+str(i))
    else:
        ftp.cwd('cycle_'+str(i))
    names = list(ftp.mlsd())
    fname = ''
    for j in range(0,len(names)):
        if names[j][0][16:19] == '052':
            fname = names[j][0]
            break
    if fname == '':
        ftp.cwd('../')
        continue
    with open(fname, "wb") as file:
    # use FTP's RETR command to download the file
        ftp.retrbinary(f"RETR {fname}", file.write)
    ftp.cwd('../')
    print('cycle ' + str(i) + ':' + ' done')



