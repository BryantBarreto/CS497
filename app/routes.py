from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app

@app.route('/')
def home():
    return render_template('main.html') #you can pass in data on init here maybe load the model

@app.route('/predict', methods=['POST'])        
def load():
   
    #jsonData = request.get_json(force=True)
    
    #image=jsonData['image']
  
   
                   
    return jsonify("return if hotdog here")