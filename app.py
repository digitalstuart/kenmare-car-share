import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'car_share'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

"""
Main page route; lifts sorted by most recent and limit on number shown
"""


@app.route('/')
@app.route('/lifts')
def lifts():
    lifts = mongo.db.lifts.find().sort('_id', -1).limit(6)
    return render_template("lifts.html", lifts=lifts)

"""
New lifts can be added; dropdown menus populated with pre-defined text
"""


@app.route('/add_lift')
def add_lift():
    locations = mongo.db.locations.find()
    whereFrom = mongo.db.locations.find()
    return render_template("add_lift.html", whereTo=locations,
                           whereFrom=whereFrom)

"""
New lift details inserted into database; redirects to main page
"""


@app.route('/list_lift', methods=['POST'])
def list_lift():
    lifts = mongo.db.lifts
    lifts.insert_one(request.form.to_dict())
    return redirect(url_for('lifts'))

"""
Route for reply form; fields populated with original lift details
"""


@app.route('/reply_to/<lift_id>')
def reply_to(lift_id):
    the_lift = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    lifts = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    locations = mongo.db.locations.find()
    whereFrom = mongo.db.locations.find()
    return render_template("reply_to.html", lift=the_lift, liftDetails=lifts,
                           whereTo=locations, whereFrom=whereFrom)

"""
Reply added to existing database document in an array
"""


@app.route('/add_reply/<lift_id>', methods=['POST'])
def add_reply(lift_id):
    mongo.db.lifts.find_one_and_update({"_id": ObjectId(lift_id)},
                                       {'$push': {"comments": {
                                        "text": request.form.get("text"),
                                        "posted": datetime.now().strftime
                                        ("%H:%M on %d/%m/%y")
                                        }}
                                        })
    return redirect(url_for('lifts'))

"""
Route for edit form; fields populated with original lift details
"""


@app.route('/edit_lift/<lift_id>')
def edit_lift(lift_id):
    the_lift = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    lifts = mongo.db.lifts.find_one({"_id": ObjectId(lift_id)})
    locations = mongo.db.locations.find()
    whereFrom = mongo.db.locations.find()
    return render_template("edit_lift.html", lift=the_lift, liftDetails=lifts,
                           whereTo=locations, whereFrom=whereFrom)

"""
Edits are sent to database
"""


@app.route('/add_edit/<lift_id>', methods=['POST'])
def add_edit(lift_id):
    lifts = mongo.db.lifts
    lifts.update({'_id': ObjectId(lift_id)},
                 {'offer_or_request': request.form.get('offer_or_request'),
                  'locations_start_name': request.form.get
                  ('locations_start_name'),
                  'locations_end_name': request.form.get('locations_end_name'),
                  'journey_details': request.form.get('journey_details'),
                  'date_of_travel': request.form.get('date_of_travel'),
                  "comments": {
                              "text": request.form.get("text"),
                              "posted": datetime.now().strftime
                              ("%H:%M on %d/%m/%y")
                              }
                  }
                 )
    return redirect(url_for('lifts'))

"""
Route for deleting a document from database
"""


@app.route('/delete_lift/<lift_id>')
def delete_lift(lift_id):
    mongo.db.lifts.remove({'_id': ObjectId(lift_id)})
    return redirect(url_for('lifts'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)