from app.database import db
from app.database.model.user import User as User_Model


def create_user(data):
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    age = data.get('age')
    user = User_Model(first_name, last_name, age)
    db.session.add(user)
    db.session.commit()


def delete_user(id):
    post = User_Model.query.filter(model.User.id == id).one()
    db.session.delete(post)
    db.session.commit()


def update_user(id, data):
    user = User_Model.query.filter(User_Model.id == post_id).one()
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.age = data.get('age')
    db.session.add(user)
    db.session.commit()
