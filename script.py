import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='KEY'
from google.cloud import vision
import re
import cv2 

def detect_usernames(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = cv2.imread(path)
    success, encoded_image = cv2.imencode('.jpg', image)
    content2 = encoded_image.tobytes()
    image_cv2 = vision.Image(content=content2)
    response =  client.text_detection(image=image_cv2)
    texts = response.text_annotations

    for text in texts:
        return text.description

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])


    if response.error.message:
        raise Exception(
            '{}\nError'.format(
                response.error.message))
        
extracted_text=detect_usernames('PATH*****')
extracted_text=extracted_text.split('\n')
filter_names=[1,4,5]
user_name=[extracted_text[i] for i in filter_names]
user_names={"username":user_name}