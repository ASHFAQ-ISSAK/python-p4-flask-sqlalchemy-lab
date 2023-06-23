from flask_sqlalchemy import SQLAlchemy
from server.app import db
from app import db

db = SQLAlchemy()


class Zookeeper(db.Model):
    __tablename__ = "zookeepers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date)


class Enclosure(db.Model):
    __tablename__ = "enclosures"

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)


class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey("zookeepers.id"))
    enclosure_id = db.Column(db.Integer, db.ForeignKey("enclosures.id"))

    zookeeper = db.relationship("Zookeeper", backref=db.backref("animals", lazy=True))
    enclosure = db.relationship("Enclosure", backref=db.backref("animals", lazy=True))
