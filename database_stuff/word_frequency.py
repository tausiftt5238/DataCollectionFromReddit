import os
import json 

with open('e_word_count.json') as file:
    data = json.loads(file.read())
    sorted_d = sorted(data.items(), key=lambda x: x[1], reverse=True)

    with open('e_sorted_word_count.json', 'w+') as output:
        json.dump(sorted_d, output)