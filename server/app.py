from flask import Flask, request, jsonify
from server.util import get_loc_names, get_estimated_prices, get_data_columns, load_saved_artifacts

load_saved_artifacts()
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
    form=request.get_json()
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

    app.run(debug=True)








































































# from flask import Flask, request, jsonify
# from server.util import get_loc_names, get_estimated_prices, get_data_columns, load_saved_artifacts

# load_saved_artifacts()
# app = Flask(__name__)

# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': get_loc_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/predict_home_price', methods=['POST'])

# def predict_home_price():
#     form = request.get_json()
#     print(form)

#     if form is None:
#         response = jsonify({
#             'error': 'Invalid JSON data. Please provide valid data.'
#         })
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response

#     try:
#         total_sqft = float(form['total_sqft'])
#         location = form['location']
#         bhk = int(form['bhk'])
#         bath = int(form['bath'])

#         estimated_price = get_estimated_prices(location, total_sqft, bhk, bath)

#         response = jsonify({
#             'estimated_price': estimated_price
#         })
#     except Exception as e:
#         response = jsonify({
#             'error': f'Error processing the request: {str(e)}'
#         })


#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# if __name__ == "__main__":
#     print("Starting python flask server for home price prediction...")

#     app.run(debug=True)



