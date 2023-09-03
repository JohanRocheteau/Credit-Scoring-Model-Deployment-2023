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
    model_name = "sk-learn-LGBMClassifier"
    stage = "Production"
    model = mlflow.sklearn.load_model(model_uri=f"models:/{model_name}/{stage}")
    
    app.run(port=8080, debug=True)