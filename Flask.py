# Import libraries
from flask import Flask, request
import mlflow
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('ModelGrid.sav', 'rb'))

@app.route('/api/',methods=['POST'])

def predict():

    # Get the data from the POST request.
    data = request.get_json()
    
    # Make prediction using model loaded from disk as per the data.
    prediction = np.array2string(model.predict_proba(data)) 
    
    # Take the first value of prediction    
    return prediction

if __name__ == '__main__':
    #model = mlflow.sklearn.load_model(model_uri)
    
    app.run(host="0.0.0.0", port=3000, debug=True)