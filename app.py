import flask
import requests
import json
from flask import request, url_for, render_template, redirect


app = flask.Flask(__name__)

mapbox_access_token = '' #mapbox api
URL = "https://geocode.search.hereapi.com/v1/geocode"
api_key = '' #hereapi

@app.route('/',methods=['GET','POST'])
def my_maps():
    return render_template('index.html',
        mapbox_access_token=mapbox_access_token)

@app.route('/getmap')
def renderlocation():
    name=request.args.get('place') 
    PARAMS = {'apikey':api_key,'q':name} 
    if name:
        print(name) 
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
 
        latitude = data['items'][0]['position']['lat']
        longitude = data['items'][0]['position']['lng']

        return render_template('greet.html',mapbox_access_token=mapbox_access_token , latitude = latitude, longitude = longitude)
    else:
        return render_template('index.html',
            mapbox_access_token=mapbox_access_token)


