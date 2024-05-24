from extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    about = db.Column(db.Text)
    avatar = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.email