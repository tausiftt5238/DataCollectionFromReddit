import requests
import os

def download_files(link, filename):
    print('downloading ' + filename + ' from the URL ' + link)

    with requests.get(link, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join('.', 'compressed data', filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        f.close()
    r.close()
    print('download complete!')