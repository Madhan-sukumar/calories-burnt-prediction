# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 13:59:14 2022

@author: Madhan
"""

from flask import Flask, render_template, request
# import requests
import pickle
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
    


app = Flask(__name__,template_folder='templates')
model = pickle.load(open('calories_burnt_prediction_model.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template("home.html")



@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender=0
        else:
            Gender=1
            
        Age=int(request.form['Age'])
        Height=float(request.form['Height'])
        Weight=float(request.form['Weight'])
        Duration=float(request.form['Duration'])
        Heart_Rate=float(request.form['Heart_Rate'])
        Body_Temp=float(request.form['Body_Temp'])
        
        

    final = np.array([[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]])
    prediction = model.predict(final)

  
    return render_template('home.html',pred='The calories burnt {}'.format(prediction))



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')