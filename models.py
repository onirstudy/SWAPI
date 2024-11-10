from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    height = db.Column(db.String(50))
    mass = db.Column(db.String(50))
    hairColor = db.Column(db.String(50))
    skinColor = db.Column(db.String(50))
    eyeColor = db.Column(db.String(50))
    birthYear = db.Column(db.String(50))
    gender = db.Column(db.String(50))

    def __init__(self, name, height, mass, hairColor, skinColor, eyeColor, birthYear, gender):
        self.name = name
        self.height = height
        self.mass = mass
        self.hairColor = hairColor
        self.skinColor = skinColor
        self.eyeColor = eyeColor
        self.birthYear = birthYear
        self.gender = gender

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hairColor': self.hairColor,
            'skinColor': self.skinColor,
            'eyeColor': self.eyeColor,
            'birthYear': self.birthYear,
            'gender': self.gender
        }
