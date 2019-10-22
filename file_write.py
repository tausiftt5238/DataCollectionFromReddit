import os
import sys
import io 
import json

def file_write(scrapped_data, filename, subreddit):
    print('initiating writing of scrapped data to file: ' + filename)
    if filename[-2:] == 'xz':
        ext = 3
    else:
        ext = 4
    with open(os.path.join('.','data for '+ subreddit +' subreddit',
        filename[:-ext] + '_' + subreddit + '.json',), 'w') as outfile:
        json.dump(scrapped_data, outfile)
        print("done with: " + filename[:-ext])
        outfile.close()
    print('write complete!')