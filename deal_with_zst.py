from zst_file_read import zst_file_read
from zst_file_write import zst_file_write

def deal_with_zst(scrapped_data, filename):
    zst_file_read(scrapped_data, filename)
    zst_file_write(scrapped_data, filename)
