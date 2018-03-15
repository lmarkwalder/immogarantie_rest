from app.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(128))
    age = db.Column(db.Integer)

    def __init__(self, first_name=first_name, last_name=last_name, age=age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return '<User %s %s - Age %d>' % \
            (self.first_name, self.last_name, self.age)
