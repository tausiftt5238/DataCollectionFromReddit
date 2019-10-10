from zst_file_read import zst_file_read
from file_write import file_write

def deal_with_zst(scrapped_data, filename, subreddit):
    zst_file_read(scrapped_data, filename, subreddit)
    file_write(scrapped_data, filename)
