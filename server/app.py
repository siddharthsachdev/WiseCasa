from flask import Flask, request, jsonify
# import util
# from server import util
from server.util import get_loc_names, get_estimated_prices, get_data_columns, load_saved_artifacts
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': get_loc_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])

def predict_home_price():
    form=dict(request.form)
    print(form)
    total_sqft = float(form['total_sqft'])
    location = form['location']
    bhk = int(form['bhk'])
    bath = int(form['bath'])

    response = jsonify({
        'estimated_price': get_estimated_prices(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting python flask server for home price prediction...")
    load_saved_artifacts()
    app.run(debug=True)


# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', "*")
#     return response
#
# @app.route('/predict_home_price',methods=['GET', 'POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])
#
#     response = jsonify({
#         'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
