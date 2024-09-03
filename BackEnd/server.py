from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

import util 

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({'locations':util.get_location_names()})
    response.headers.add('Accesss-Control-Allow-Origin', '*')
    return response
    # return "Hi, How're u?"

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({'estimated_price':util.get_estimated_price(location, total_sqft, bhk,bath)})   
    response.headers.add('Accesss-Control-Allow-Origin', '*')
    return response 
    

if __name__ == "__main__":
    print('Starting python flask server for the prediction!!!!')
    util.load_saved_artifacts()
    app.run(debug = True)
    