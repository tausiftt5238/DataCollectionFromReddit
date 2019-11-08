import os
import json 
from read_all_files import read_all_files

comments,submissions = read_all_files('data for speedrun subreddit')

game_frequency = {"doom": 0, "quack": 0, "metroid": 0, "mario": 0, "zelda": 0,
"ocarina of time": 0, "oot": 0, "dark souls": 0}

for comment in comments:
    for x in game_frequency:
        if x in comment['body'].lower():
            game_frequency[x] += 1
    
for submission in submissions:
    for x in game_frequency:
        if x in submission['title'].lower() or x in submission['selftext'].lower():
            game_frequency[x] += 1
    
with open('game_frequncy.json', 'w+') as output:
    json.dump(game_frequency, output)