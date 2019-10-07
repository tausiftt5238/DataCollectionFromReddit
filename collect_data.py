import os
import sys
import io 
import bz2
from download_files import download_files
from deal_with_zst import deal_with_zst
from deal_with_bz2 import deal_with_bz2

scrapped_data = [] 

link = sys.argv[1]
filename = link[-14:]
download_files(link, filename)

if filename[:-3] == 'zst':
    #Deal with zst
    deal_with_zst(scrapped_data, filename)
elif filename[:-3] == 'bz2':
    #Deal with bz2
    deal_with_bz2(scrapped_data, filename)
else:
    #Deal with xz 
    print("under construction")
#Delete the downloaded file
os.remove(os.path.join('.', 'compressed data', filename))