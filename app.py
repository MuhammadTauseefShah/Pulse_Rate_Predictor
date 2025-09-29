from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input from the form
        features = [float(x) for x in request.form.values()]
        
        # Reshape for a single prediction
        final_features = np.array(features).reshape(1, -1)
        
        # Scale the features
        scaled_features = scaler.transform(final_features)
        
        # Make a prediction
        prediction = model.predict(scaled_features)
        
        output = round(prediction[0], 2)
        
        return render_template('index.html', prediction_text=f'Predicted Pulse Pressure: {output}')

if __name__ == '__main__':
    app.run(debug=True)