import os
import json 

def read_all_files(path):
    comments = []
    submissions = []
    for filename in os.listdir(path):
        
        for filename2 in os.listdir(os.path.join(path, filename)):
            
            with open(os.path.join(path, filename, filename2)) as json_file:
                #print("directory: " +filename + "subdirectory: " + filename2)
                try:    
                    data = json.loads(json_file.read())
                except:
                    data = []
                    print("failed for: " + filename2)
                for x in data:
                    if 'comments' in filename:
                        # print('this is a comments subdirectory! filename: ' + filename)
                        comments.append(x)
                    elif 'submissions' in filename:
                        # print('this is a submissions subdirectory!filename: ' + filename)
                        submissions.append(x)
    return comments, submissions

# read_all_files(os.path.join('..','data for speedrun subreddit'))