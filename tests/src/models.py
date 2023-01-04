from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)

# write a function to test the Users model
def test_users():
    user = Users(
        username="test_user",
        email="test@example.com",
        password="test_password",
    )
    assert user.username == "test_user"
    assert user.email == "test@example.com"
    assert user.password == "test_password"