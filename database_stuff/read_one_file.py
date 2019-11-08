import os
import json 

def read_one_file(path):
    comments = []
    submissions = []
    #print("directory: " +filename + "subdirectory: " + filename2)
    with open(path) as json_file:
        try:    
            data = json.loads(json_file.read())
        except:
            data = []
            #print("failed for: " + filename2)
        for x in data:
            if 'RC' in path:
                # print('this is a comments subdirectory! filename: ' + filename)
                comments.append(x)
            elif 'RS' in path:
                # print('this is a submissions subdirectory!filename: ' + filename)
                submissions.append(x)
    return comments, submissions

# read_all_files(os.path.join('..','data for speedrun subreddit'))