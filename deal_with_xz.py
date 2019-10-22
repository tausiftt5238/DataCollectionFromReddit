from xz_file_read import xz_file_read
from file_write import file_write

def deal_with_xz(scrapped_data, filename, subreddit):
    xz_file_read(scrapped_data, filename, subreddit)
    file_write(scrapped_data, filename, subreddit)
