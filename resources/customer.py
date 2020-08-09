from flask_restful import Resource, reqparse
from models.customer import CustomerModel
from flask_jwt import jwt_required


class CustomerRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number',
                        type = int,
                        required = True,
                        help = "Phone Number is required to register."
                        )
    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = "Password is required to register."
                        )
    parser.add_argument('firstname',
                        type=str,
                        required=True,
                        help="First name is required to register."
                        )
    parser.add_argument('lastname',
                        type=str,
                        required=False,
                        help="First name is required to register."
                        )
    parser.add_argument('email',
                        type=str,
                        required=False,
                        help="First name is required to register."
                        )

    def post(self):
        data = CustomerRegister.parser.parse_args()
        print(data)

        if CustomerModel.find_by_phone(data['phone_number']):
            return {"message": "Phone number already registered"}, 400

        customer = CustomerModel(data['phone_number'],data['password'],data['firstname'],data['lastname'],data['email'])
        customer.save_to_db()

        return {"message": "User registered successfully."}, 201


class CustomerDetails(Resource):
    @jwt_required()
    def get(self, phone_number):
        customer = CustomerModel.find_by_phone(phone_number)
        if customer:
            return customer.json()
        return {"message": "User not found."}, 404
