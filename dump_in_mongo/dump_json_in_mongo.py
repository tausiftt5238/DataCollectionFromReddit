from pymongo import MongoClient
from read_all_files import read_all_files
from read_one_file import read_one_file
import os 
import json 

#comments, submissions = read_all_files(os.path.join('..','data for speedrun subreddit'))
comments, submissions = read_one_file(os.path.join('.', 'data for speedrun subreddit', '2015_comments', 'RC_2015-07_speedrun.json'))

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient['reddit_speedrun']
comments_collection = mydb['comments']
x = comments_collection.insert_many((comments))
submissions_collection = mydb['submissions']
y = submissions_collection.insert_many((submissions))