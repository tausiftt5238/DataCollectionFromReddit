from read_all_files import read_all_files
import os 
from datetime import datetime
import time 
import json 

# comments, submissions = read_all_files(os.path.join('data for speedrun subreddit'))

# print(len(comments), len(submissions))
# # Do frequency count of words
words = dict()
users = {"2014": [], "2015": [], "2016": [], "2017": [], "2018": [], "2019": []}
number_of_comments =  {"2014": 0, "2015": 0, "2016": 0, "2017": 0, "2018": 0, "2019": 0}
number_of_submissions =  {"2014": 0, "2015": 0, "2016": 0, "2017": 0, "2018": 0, "2019": 0}


# for comment in comments:

# for submission in submissions:
path = os.path.join('data for speedrun subreddit')
for filename in os.listdir(path):
        
    for filename2 in os.listdir(os.path.join(path, filename)):
        
        with open(os.path.join(path, filename, filename2)) as json_file:
            #print("directory: " +filename + "subdirectory: " + filename2)
            year = filename[:4]
            try:    
                data = json.loads(json_file.read())
            except:
                data = []
                print("failed for: " + filename2)
            #json.loads(json_file.read())
            for x in data:
                if 'comments' in filename:
                    # Getting name of the users in each year 
                    if x['author'] != '[deleted]' and x['author'] not in users[year]:
                        users[year].append(x['author'])

                    #Iterating through all of the words in a string to do frequency count of words
                    split = x['body'].split()
                    for y in split:
                        if y in words:
                            words[y] += 1
                        else:
                            words[y] = 1
                elif 'submissions' in filename:
                    # Getting name of the users in each year 
                    if x['author'] != '[deleted]' and x['author'] not in users[year]:
                        users[year].append(x['author'])

                    #Iterating through all of the words in a string to do frequency count of words
                    split = x['title'].split()
                    for y in split:
                        if y in words:
                            words[y] += 1
                        else:
                            words[y] = 1

                    #Iterating through all of the words in a string to do frequency count of words
                    split = x['selftext'].split()
                    for y in split:
                        if y in words:
                            words[y] += 1
                        else:
                            words[y] = 1

                if x['author_flair_text'] in words:
                    words[x['author_flair_text']] += 1
                else:
                    words[x['author_flair_text']] = 1
            if 'comments' in filename:
                number_of_comments[year] += len(data)
            elif 'submissions' in filename:
                number_of_submissions[year] += len(data)
# print(users)
# print(number_of_comments)
# print(number_of_submissions)
# print(words)
print("Done")

with open('users_stats.json', 'w+') as output:
    output.write(json.dumps(users))

with open('number_of_comments.json', 'w+') as output:
    output.write(json.dumps(number_of_comments))

with open('number_of_submissions.json', 'w+') as output:
    output.write(json.dumps(number_of_submissions))

with open('word_count.json', 'w+') as output:
    output.write(json.dumps(words))