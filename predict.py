from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import os
import requests
import bs4
from urllib.request import urlopen
from PIL import Image

def pred(image, model_path_load=''):
    # Load model
    model = load_model(model_path_load)

    img_array = img_to_array(image)
    img_array /= 255
    img_array = np.expand_dims(img_array, 0)

    return model.predict(img_array)

def get_image(path):
    req = requests.get(path)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    print('soup: ', soup)
    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        print('link: ', link)
        if link:
            print('Source: {}'.format(link))
    img = Image.open(urlopen(link))
    img = img.resize((150,150))
    return img

def get_catdog(path):
    model_path = './cat_dog_classification_model.h5'
    img = get_image(path)
    pred_score = pred(img, model_path_load=model_path)
    score = pred_score[0]
    res = "This image is %.2f percent cat and %.2f percent dog." % (100 * (1 - score), 100 * score)
    return {'result':res} #, 'img':img}

def get_cd(img):
    model_path = './cat_dog_classification_model.h5'
    pred_score = pred(img, model_path_load=model_path)
    score = pred_score[0]
    res = "This image is %.2f percent cat and %.2f percent dog." % (100 * (1 - score), 100 * score)
    return {'result':res}

if __name__ == '__main__':
    path = 'https://images.app.goo.gl/BD3awL9deRre1b3F6'
    print('path: ', path)
    res = get_catdog(path)
    print(res)
    