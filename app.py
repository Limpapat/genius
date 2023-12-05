import json
import time
from flask import Flask, request, render_template
# from flask_restful import Resource, Api, reqparse
# import requests
from predict import *
# from urllib.parse import unquote, quote
# import matplotlib.pyplot as plt

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# api = Api(app)

@app.route('/')
def index(name=None):
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f= request.files['filename']
        print("!!!", f)
        img = Image.open(f)
        img = img.resize((150,150))
        # f.save(os.path.join (app.config['UPLOAD_FOLDER'],f.filename))
        res = get_cd(img)
        return res['result']

# class get_catordog(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('path', type=str)
#         dictp = parser.parse_args()
#         kw = unquote(dictp['path'])
#         print('kw: ', kw)
#         res = get_catdog(kw)
#         return res

# api.add_resource(get_catordog, '/get_catordog',endpoint='get_catordog')
if __name__ == '__main__':
    app.run(threaded=True)
