from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [
            float(request.form['Nitrogen']),
            float(request.form['Phosphorus']),
            float(request.form['Potassium']),
            float(request.form['Temperature']),
            float(request.form['Humidity']),
            float(request.form['ph']),
            float(request.form['Rainfall'])
        ]
        
        # Make prediction
        prediction = model.predict([features])[0]
        
        return render_template('index.html', 
                            prediction_text=f'Recommended Crop: {prediction}',
                            show_result=True)
    
    except Exception as e:
        return render_template('index.html', 
                            prediction_text=f'Error: {str(e)}',
                            show_result=True)

if __name__ == '__main__':
    app.run(debug=True)