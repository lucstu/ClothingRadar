from siaskynet import Skynet
import requests
import shutil
import os
import json

def download_and_upload(image_url):
    filename = image_url.split("/")[-1]
    filename = filename.split('?')[0]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)

        skylink = Skynet.upload_file(filename)
        if skylink is not None:
            os.remove(filename)
            return skylink
    else:
        print('Image Couldn\'t be retreived')
        return None

f = open('sample.json',)

data = json.load(f)

for d in data:
    newLink = download_and_upload(d['image'])
    d['image'] = newLink

with open('newsample.json', 'w') as out:
    json.dump(data, out)

f.close()