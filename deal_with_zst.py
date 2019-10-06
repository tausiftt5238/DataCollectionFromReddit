import os
import sys
import io 
import bz2
from download_files import download_files
from zst_file_read import zst_file_read
from zst_file_write import zst_file_write

scrapped_data = [] 

link = sys.argv[1]
filename = link[-14:]
download_files(link, filename)

#zst_file_read(scrapped_data, filename)
#zst_file_write(scrapped_data, filename)

#Delete the downloaded file
#os.remove(os.path.join('.', 'compressed data', filename))