from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security.customer import authenticate, identity
from resources.customer import CustomerRegister, CustomerDetails

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'h2h'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(CustomerRegister, '/register')
api.add_resource(CustomerDetails, '/user_detail/<phone_number>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)