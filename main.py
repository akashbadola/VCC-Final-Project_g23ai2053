# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Make prediction
    prediction = model.predict(final_features)

    if prediction[0] == 0:
        output ="This Customer falls in cluster - 0 , with high income and low spending"
    elif prediction[0] == 1:
        output ="This Customer falls in cluster - 1 , with moderate income and moderate spending"
    elif prediction[0] == 2:
        output ="This Customer falls in cluster - 2 , with high income and high spending"
    elif prediction[0] == 3:
        output ="This Customer falls in cluster - 3 , with low income and high spending"
    elif prediction[0] == 4:
        output ="This Customer falls in cluster - 4 , with low income and low spending"

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
