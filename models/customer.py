from db import db


class CustomerModel(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(70))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(50))

    def __init__(self, phone, password, first_name, last_name, email):
        self.phone = phone
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def json(self):
        return {'phone_number':self.phone, 'firstname':self.first_name, 'lastname':self.last_name, 'password':self.password, 'email':self.email}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_phone(cls, phone_number):
        return cls.query.filter_by(phone=phone_number).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()