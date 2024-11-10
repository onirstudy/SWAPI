import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///swapi.db'  # You can change it to MySQL or other DBs
    SQLALCHEMY_TRACK_MODIFICATIONS = False
