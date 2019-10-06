import os
import sys
import io 
import json

def zst_file_write(scrapped_data, filename):
    print('initiating writing of scrapped data to file: ' + filename)
    with open(os.path.join('.','data for speedrun subreddit',
        filename[:-4] + '_speedrun.json',), 'w') as outfile:
        json.dump(scrapped_data, outfile)
        print("done with: " + filename[:-4])
        outfile.close()
    print('write complete!')