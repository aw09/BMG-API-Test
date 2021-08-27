from app import db

class User(db.Model):
    __tablename__ = 'stadium'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password, name, email, ref=''):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.ref = ref

    # def __repr__(self):
    #     return f'Id: {self.id}. {self.name} is the home of the {self.team}'