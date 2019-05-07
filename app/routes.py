from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from app import app
import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python import keras
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.applications.resnet50 import preprocess_input
import os

UPLOAD_FOLDER = 'C:/Users/bryan/Documents/CS497/AIFinal/app/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('main.html') #you can pass in data on init here maybe load the model before running anything

@app.route('/predict', methods=['POST'])        
def load():
    #do model stuff here and return string of hotdog or not

    f = request.files['img']

    filename = secure_filename(f.filename)

    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # path = url_for('img',
    #                         filename=filename)

    model = load_model('C:/Users/bryan/Documents/CS497/AIFinal/app/final_hotdog_model.h5')

    def read_and_prep_image(img_path, img_height=224, img_width=224):
        imgs = [load_img(img_path, target_size=(img_height, img_width))]
        img_array = np.array([img_to_array(img) for img in imgs])
        output = preprocess_input(img_array)
        return(output)

    image_data = read_and_prep_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    result = model.predict(image_data)

    if(np.argmax(result[0]) == 0):
        return jsonify('Hot Dog')
    else:
        return jsonify('Not Hot Dog')

    jsonData = request.get_json(force=True)
    test = jsonData['test']
                   
    return jsonify(test)