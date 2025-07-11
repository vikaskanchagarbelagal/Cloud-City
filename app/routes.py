from flask import render_template, request, redirect, url_for
from app import app, mongo
from bson.objectid import ObjectId

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    properties = mongo.db['Cloud-City'].find()  # Use the collection name 'Cloud-City'
    return render_template('dashboard.html', properties=properties)

@app.route('/add_property', methods=['POST'])
def add_property():
    data = request.form
    mongo.db['Cloud-City'].insert_one({
        "name": data.get("name"),
        "owner": data.get("owner"),
        "price": float(data.get("price")),
        "description": data.get("description")
    })
    return redirect(url_for('dashboard'))

@app.route('/update_property/<property_id>', methods=['POST'])
def update_property(property_id):
    data = request.form
    mongo.db['Cloud-City'].update_one(
        {"_id": ObjectId(property_id)},
        {"$set": {
            "name": data.get("name"),
            "owner": data.get("owner"),
            "price": float(data.get("price")),
            "description": data.get("description")
        }}
    )
    return redirect(url_for('dashboard'))

@app.route('/delete_property/<property_id>', methods=['POST'])
def delete_property(property_id):
    mongo.db['Cloud-City'].delete_one({"_id": ObjectId(property_id)})
    return redirect(url_for('dashboard'))
