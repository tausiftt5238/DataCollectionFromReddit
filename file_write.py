import os
import sys
import io 
import json

def file_write(scrapped_data, filename):
    print('initiating writing of scrapped data to file: ' + filename)
    if filename[-2:] == 'xz':
        ext = 3
    else:
        ext = 4
    with open(os.path.join('.','data for speedrun subreddit',
        filename[:-ext] + '_speedrun.json',), 'w') as outfile:
        json.dump(scrapped_data, outfile)
        print("done with: " + filename[:-ext])
        outfile.close()
    print('write complete!')