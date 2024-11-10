from flask import Flask, request, jsonify,render_template
import requests,os,sys
from models import db, Person
from config import Config

sys.dont_write_bytecode = True


app = Flask(__name__)
app.config.from_object(Config) 
db.init_app(app)

# Create the database tables (if they don't already exist)
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/getAllData', methods=['GET'])
def getAllData():
    try:
        # Query all people from the database
        people = Person.query.all()
        
        # If no data is found, return a message
        if not people:
            return jsonify({"message": "No data found!"}), 404

        # Convert the list of people objects to a list of dictionaries
        peopleList = [person.toDict() for person in people]
        
        return jsonify(peopleList), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/fetchData', methods=['GET'])
def fetchData():
    try:
        response = requests.get("https://swapi.dev/api/people/")
        data = response.json()

        for item in data['results']:
            person = Person(
                name=item['name'],
                height=item['height'],
                mass=item['mass'],
                hairColor=item['hair_color'],
                skinColor=item['skin_color'],
                eyeColor=item['eye_color'],
                birthYear=item['birth_year'],
                gender=item['gender']
            )
            db.session.add(person)
        db.session.commit()
        return jsonify({"message": "Data fetched and saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500






@app.route('/editData/<int:id>', methods=['PUT'])
def editData(id):
    data = request.get_json()
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Person not found!"}), 404

    for key, value in data.items():
        if hasattr(person, key):
            setattr(person, key, value)
    db.session.commit()

    return jsonify({"message": "Person data updated successfully!"}), 200

@app.route('/getData/<int:id>', methods=['GET'])
def getData(id):
    person = Person.query.get(id)
    if person:
        return jsonify(person.toDict()), 200
    return jsonify({"message": "Person not found!"}), 404

@app.route('/deleteData/<int:id>', methods=['DELETE'])
def deleteData(id):
    person = Person.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully!"}), 200
    return jsonify({"message": "Person not found!"}), 404

import sys

# Prevent Python from writing bytecode (.pyc files)
sys.dont_write_bytecode = True

if __name__ == '__main__':
    app.run(debug=True)
