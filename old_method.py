import json
import os
import sys
import io 

def scrap_subreddit(scrapped_data, subreddit, filename):

    with open(filename, 'r') as read_file:
        #print('currently running: ' + read_file.name)
        for x in read_file:

            try:
                data = json.loads(x)
                if data['subreddit'] == subreddit:
                    scrapped_data.append(data)
            except Exception as e:
                print(e)
    read_file.close()


scrapped_data = []
for filename in os.listdir('F:\projects\cscw\\'+sys.argv[0][2:-3]+'\scrap_the_data'):
    scrap_subreddit(scrapped_data, 'speedrun', 'F:\projects\cscw\\'+sys.argv[0][2:-3]+'\scrap_the_data\\' + filename)

with open('F:\projects\cscw\data for speedrun subreddit\\'+sys.argv[0][2:-3]+'_speedrun.json', 'w') as outfile:
    json.dump(scrapped_data, outfile)
outfile.close()
