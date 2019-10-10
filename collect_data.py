import os
import sys
import io 
import bz2
from download_files import download_files
from deal_with_zst import deal_with_zst
from deal_with_bz2 import deal_with_bz2
from deal_with_xz import deal_with_xz

scrapped_data = [] 

link = sys.argv[1]
subreddit = sys.argv[2]
filename = link[-14:]
if not filename[-3:] == 'zst' or filename[-3:] == 'bz2':
    filename = link[-13:]
download_files(link, filename)

if filename[-3:] == 'zst':
    #Deal with zst
    deal_with_zst(scrapped_data, filename, subreddit)
elif filename[-3:] == 'bz2':
    #Deal with bz2
    deal_with_bz2(scrapped_data, filename, subreddit)
else:
    #Deal with xz 
    deal_with_xz(scrapped_data, filename, subreddit)
    
#Delete the downloaded file
os.remove(os.path.join('.', 'compressed data', filename))