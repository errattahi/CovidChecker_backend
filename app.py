import os

from flask import Flask, request, render_template, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import pandas as pd
import numpy as np
from werkzeug.utils import secure_filename
from datetime import date, datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/covid_ai_db"
# app.config['MONGO_DBNAME'] = 'images'
app.config['SECRET_KEY'] = ''

mongo = PyMongo(app)
db = mongo.db
imagesCol = mongo.db["images"]
personsCol = mongo.db["persons"]
# print("MongoDB Database:", mongo.db)

model = load_model('.\model\\best_InceptionV3_covid19_trainall_Config6_Holdout_Binary.h5')


def read_pil_image(img_path):
    with open(img_path, 'rb') as f:
        im = Image.open(f)
        width, height = im.size
        return np.array(im.convert('RGB').resize((height, width)))


def model_predict(img_path, model):
    img = np.array([read_pil_image(img_path)])
    test_datagen = ImageDataGenerator(rescale=1. / 255,
                                      )
    prediction = model.predict(test_datagen.flow(img))
    return prediction


@app.route('/', methods=['GET'])
def index():
    # Main Page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        imagesCol.insert_one({'path': file_path, 'date': datetime.now(), 'user_id': f.filename.split(".")[0]})

        # Make a prediction
        prediction = model_predict(file_path, model)
        print(prediction[0])

    return str(round(prediction[0][0] * 100, 2))


@app.route('/saveUser', methods=['POST'])
def save_user():
    gender = request.json['gender']
    age = request.json['age']
    region = request.json['region']
    smoker = request.json['smoker']
    pcr = request.json['pcr']
    last_pcr = request.json['last_pcr']
    diseases = request.json['diseases']
    symptoms = request.json['symptoms']

    if last_pcr == "":
        _id = personsCol.insert_one(
            {'gender': gender, 'age': age, 'region': region, 'smoker': smoker, 'pcr': pcr, 'diseases': diseases,
             'symptoms': symptoms})
    else:
        _id = personsCol.insert_one(
            {'gender': gender, 'age': age, 'region': region, 'smoker': smoker, 'pcr': pcr, 'last_pcr': last_pcr,
             'diseases': diseases,
             'symptoms': symptoms})
    # print(_id.inserted_id)

    return str(_id.inserted_id)


if __name__ == '__main__':
    app.run()

# flask run --host=0.0.0.0
