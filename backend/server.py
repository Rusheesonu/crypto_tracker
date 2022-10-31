# Import flask and datetime module for showing date and time
from flask import Flask
import datetime
from flask_cors import CORS, cross_origin
import json
import requests
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin() 
# Route for seeing a data
@app.route('/crypto_data')
def get_crypto_data():

    return_data = {}
    r = requests.get("https://api.coinstats.app/public/v1/coins?skip=0&limit=50&currency=USD")
    coins_data = r.content
    return coins_data
  
    # Returning an api for showing in  reactjs

      
# Running app
if __name__ == '__main__':
    app.run(debug=True)

