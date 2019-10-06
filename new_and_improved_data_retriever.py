import json
import os
import sys
import io 
import zstandard as zstd 


def scrap_subreddit(scrapped_data, subreddit, obj):

    try:
        if obj['subreddit'] == subreddit:
            # print(obj)
            scrapped_data.append(obj)
    except Exception as e:
        pass

for filename in os.listdir('F:\projects\cscw\compressed data'):
    scrapped_data = []
    with open('F:\projects\cscw\compressed data\\' + filename, 'rb') as fh:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(fh) as reader:
            previous_line = ""
            while True:
                chunk = reader.read(2**27)
                if not chunk:
                    break

                string_data = chunk.decode('utf-8')
                lines = string_data.split("\n")
                for i, line in enumerate(lines[:-1]):
                    if i == 0:
                        line = previous_line + line
                    try:
                        object = json.loads(line)
                        scrap_subreddit(scrapped_data, 'speedrun', object)
                    except Exception as e:
                        pass
                previous_line = lines[-1]


    with open('F:\projects\cscw\data for speedrun subreddit\\'+filename[:-4]+'_speedrun.json', 'w') as outfile:
        json.dump(scrapped_data, outfile)
    print("done with " + filename[:-4])
    outfile.close()