
#importing flask modules

from flask import Flask, render_template, request
from bson.objectid import ObjectId
from flask.json import JSONEncoder, jsonify

from flask_pymongo import PyMongo


# initializing a variable of Flask
app = Flask(__name__)

app.config['MONGO_DBNAME']='crime'

app.config['MONGO_URI'] = 'mongodb://localhost:27017/crime'

mongo = PyMongo(app)

app.json_encoder = JSONEncoder

# decorating index function with the app.route with url as /login
@app.route('/crime')
def index():
   return render_template('crime.html')


@app.route('/FlaskTutorial',  methods=['GET', 'POST', 'DELETE', 'PATCH'])

def success(crimeId=None):
   if request.method == 'POST':
       crimeId = request.form['crimeId']
       query = request.args
       data = mongo.db.crime.find_one({"_id":crimeId})
       return jsonify(data), 200

   else:
       pass

if __name__ == "__main__":
   app.run()
