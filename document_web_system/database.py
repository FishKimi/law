from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rating(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user = db.Column(db.String(100))

    document = db.Column(db.String(200))

    question = db.Column(db.String(200))

    score = db.Column(db.Integer)

    note = db.Column(db.Text)