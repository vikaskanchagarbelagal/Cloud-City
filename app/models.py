from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Property {self.name}>'
