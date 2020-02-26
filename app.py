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
    locations = mongo.db.locations.find()
    whereFrom = mongo.db.locations.find()
    return render_template("add_lift.html", whereTo = locations, whereFrom = whereFrom)

@app.route('/list_lift', methods=['POST'])
def list_lift():
    lifts = mongo.db.lifts
    lifts.insert_one(request.form.to_dict())
    return redirect(url_for('lifts'))

@app.route('/reply_to/<lift_id>')
def reply_to(lift_id):
    the_lift = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    lifts = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    locations = mongo.db.locations.find()
    whereFrom = mongo.db.locations.find()
    return render_template("reply_to.html", lift=the_lift, liftDetails=lifts,
                           whereTo = locations, whereFrom = whereFrom)

@app.route('/add_reply/<lift_id>', methods=['POST'])
def add_reply(lift_id):
    lifts = mongo.db.lifts
    lifts.update( {'_id': ObjectId(lift_id)},
    {   'offer_or_request':request.form.get('offer_or_request'),
        'locations_start_name':request.form.get('locations_start_name'),
        'locations_end_name': request.form.get('locations_end_name'),
        'journey_details': request.form.get('journey_details'),
        'reply':request.form.get('reply')
    })
    return redirect(url_for('lifts'))

@app.route('/edit_lift/<lift_id>')
def edit_lift(lift_id):
    the_lift = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    lifts = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    locations = mongo.db.locations.find()
    whereFrom = mongo.db.locations.find()
    return render_template("edit_lift.html", lift=the_lift, liftDetails=lifts,
                           whereTo = locations, whereFrom = whereFrom)

@app.route('/add_edit/<lift_id>', methods=['POST'])
def add_edit(lift_id):
    lifts = mongo.db.lifts
    lifts.update( {'_id': ObjectId(lift_id)},
    {   'offer_or_request':request.form.get('offer_or_request'),
        'locations_start_name':request.form.get('locations_start_name'),
        'locations_end_name': request.form.get('locations_end_name'),
        'journey_details': request.form.get('journey_details'),
    })
    return redirect(url_for('lifts'))

@app.route('/delete_lift/<lift_id>')
def delete_lift(lift_id):
    mongo.db.lifts.remove({'_id': ObjectId(lift_id)})
    return redirect(url_for('lifts'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)