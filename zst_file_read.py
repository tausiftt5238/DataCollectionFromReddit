from scrap_subreddit import scrap_subreddit
import zstandard as zstd 
import json
import os 

def zst_file_read(scrapped_data, filename):
    print('starting to read file: ' + filename)
    with open(os.path.join('.', 'compressed data', filename), 'rb') as fh:
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
                    except Exception:
                        pass
                previous_line = lines[-1]
    print('done reading!')