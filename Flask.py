# Import libraries
from flask import Flask, request
import mlflow
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/api/',methods=['POST'])

def predict():

    # Get the data from the POST request.
    data = request.get_json()
    
    # Make prediction using model loaded from disk as per the data.
    prediction = np.array2string(model.predict_proba(data)) 
    
    
    # Take the first value of prediction    
    return prediction

if __name__ == '__main__':
    # Load the model
    model = pickle.load(open('ModelGrid.sav', 'rb'))
    #model = mlflow.sklearn.load_model(model_uri)
    
    #app.run(port=8080, debug=True)