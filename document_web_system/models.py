from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True)

    role = db.Column(db.String(10))


class Document(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    content = db.Column(db.Text)


class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    document_id = db.Column(db.Integer)

    question = db.Column(db.String(200))

    description = db.Column(db.Text)


class Score(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    document_id = db.Column(db.Integer)

    question_id = db.Column(db.Integer)

    score = db.Column(db.Integer)