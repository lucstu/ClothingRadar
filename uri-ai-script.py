import io
import os
from csv import reader
import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

def detect_labels_uri(uri):

    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    labelList = []
    for label in labels:
        #print(label.description)
        labelList.append(label.description)

    return labelList
        

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))



def write_to_json(name, labels, image, product):
    new_item = {"name": name,
                "labels": labels,
                "image": image,
                "product": product}
    
    json_object = json.dumps(new_item, indent = 4)

    with open("sample.json", "a") as outfile: 
        outfile.write(json_object)
        print("done!")

with open('short-list.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        name = row[0]
        link = row[1]
        product = row[2]
        print(name)
        
        labels = detect_labels_uri(link)
        write_to_json(name, labels, link, product)
        
        



