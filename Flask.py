# Import libraries
from flask import Flask, request
import mlflow
import numpy as np

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
    model_uri = "mlflow-artifacts:/8cef877a90864d9ea9a1432b58f8e5d3/dd8c1ebb7e1b4929bcbc968736cf8e0d/artifacts/sklearn-model"
    model = mlflow.sklearn.load_model(model_uri)
    
    app.run(port=8080, debug=True)