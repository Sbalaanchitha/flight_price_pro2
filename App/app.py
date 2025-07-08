from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join('model', 'model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form

        features = [
            int(data['Total_Stops']),
            int(data['Duration']),
            int(data['Journey_day']),
            int(data['Journey_month']),
            int(data['Dep_hour']),
            int(data['Dep_min']),
            int(data['Arrival_hour']),
            int(data['Arrival_min']),

            # Airline (1-of-n encoding)
            int(data.get('Airline_Air India', 0)),
            int(data.get('Airline_IndiGo', 0)),
            int(data.get('Airline_Multiple carriers', 0)),
            int(data.get('Airline_SpiceJet', 0)),
            int(data.get('Airline_Vistara', 0)),
            int(data.get('Airline_GoAir', 0)),
            int(data.get('Airline_Trujet', 0)),
            int(data.get('Airline_Jet Airways', 0)),

            # Source
            int(data.get('Source_Delhi', 0)),
            int(data.get('Source_Kolkata', 0)),
            int(data.get('Source_Mumbai', 0)),
            int(data.get('Source_Bangalore', 0)),

            # Destination
            int(data.get('Destination_BLR', 0)),
            int(data.get('Destination_Cochin', 0)),
            int(data.get('Destination_Delhi', 0)),
            int(data.get('Destination_Hyderabad', 0)),
            int(data.get('Destination_Kolkata', 0)),
            int(data.get('Destination_Chennai', 0)),
            int(data.get('Destination_Jaipur', 0)),
            int(data.get('Destination_Goa', 0))
        ]

        prediction = model.predict([features])[0]
        output = round(prediction, 2)

        return render_template('index.html', prediction_text=f"Estimated Flight Price: ₹{output}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
