import os
import sys
import io 
import bz2
from download_files import download_files
from bz2_file_read import bz2_file_read
from zst_file_write import zst_file_write

scrapped_data = [] 

link = sys.argv[1]
filename = link[-14:]
download_files(link, filename)
bz2_file_read(scrapped_data, filename)
#It works for extensions that have length of 3, so it's fine
zst_file_write(scrapped_data, filename)

#Delete the downloaded file
os.remove(os.path.join('.', 'compressed data', filename))