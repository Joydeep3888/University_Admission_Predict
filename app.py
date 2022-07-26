from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  r2_score

app=Flask(__name__) #initializing the flask app
@app.route('/', methods=['GET','POST'])#route to display the home page
@cross_origin()

def homepage():
    return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
@cross_origin()
def index():
    if request.method=='POST':
        try:
            gre_score=float(request.form['gre_score'])
            toefl_score=float(request.form['toefl_score'])
            university_rating=float(request.form['university_rating'])
            sop=float(request.form['sop'])
            lor=float(request.form['lor'])
            cgpa=float(request.form['cgpa'])
            Research_done=request.form['research']
            if Research_done=='yes':
                research=1
            else:
                research=0
            file_name='admission_linear_model.pickle'
            model=pickle.load(open(file_name, 'rb'))
            predictions=model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            print('the pridction of the model is', predictions)
            return render_template('results.html', preditions=np.round(predictions))
        except Exception as e:
            print('There is some exception', e)
            return('somthing is wrong', e)
    else:
        return render_template('index.html')

if __name__=="__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)










