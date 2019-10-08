from scrap_subreddit import scrap_subreddit
import json
import os 
import lzma

def xz_file_read(scrapped_data, filename):
    print('starting to read file: ' + filename)
    #iteration = 1
    with lzma.open(os.path.join('.', 'compressed data', filename), 'rb') as fh:
        while True:
            chunk = fh.read(2**25)
            previous_line = ""
            if not chunk:
                break

            string_data = chunk.decode('utf-8')
            lines = string_data.split("\n")
            for i, line in enumerate(lines[:-1]):
                if i == 0 :
                    line = previous_line + line 
                try:
                    object = json.loads(line)
                    scrap_subreddit(scrapped_data, 'speedrun', object)
                except Exception:
                    pass
                #print('iteration number: ' + str(i))
            previous_line = lines[-1]
            # print("iteration: " + str(iteration))
            # iteration += 1
    print('done reading!')