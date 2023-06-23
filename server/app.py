#!/usr/bin/env python3

from flask import Flask
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return "<h1>Zoo app</h1>"


@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.get(id)
    return f"<h1>Animal: {animal.name}</h1>"


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    return f"<h1>Zookeeper: {zookeeper.name}</h1>"


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    return f"<h1>Enclosure: {enclosure.environment}</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
