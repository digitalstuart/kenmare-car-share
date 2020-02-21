import os
from os import path
if path.exists("env.py"):
    import env 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'car_share' 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/lifts')
def lifts():
    return render_template("lifts.html", lifts=mongo.db.lifts.find())

@app.route('/add_lift')
def add_lift():
    return render_template("add_lift.html",
    locations=mongo.db.locations.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)