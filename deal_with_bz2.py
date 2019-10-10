from bz2_file_read import bz2_file_read
from file_write import file_write

def deal_with_bz2(scrapped_data, filename, subreddit):
    bz2_file_read(scrapped_data, filename, subreddit)
    #It works for extensions that have length of 3, so it's fine
    file_write(scrapped_data, filename)
