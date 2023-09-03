# Import libraries
from flask import Flask, request
import mlflow

app = Flask(__name__)

# Load the model
model_name = "sk-learn-LGBMClassifier"
stage = "Production"

model = mlflow.sklearn.load_model(model_uri=f"models:/{model_name}/{stage}")


@app.route('/api',methods=['POST'])

def predict():
    if request.method == 'POST':
        # Get the data from the POST request.
        features = request.form.values()
        
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict_proba(features)    
        
        # Take the first value of prediction    
        return prediction

if __name__ == '__main__':
    app.run(port=8080, debug=True)