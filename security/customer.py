from werkzeug.security import safe_str_cmp
from models.customer import CustomerModel


def authenticate(username, password):
    print(username,password)
    customer = CustomerModel.find_by_phone(username)
    if customer and safe_str_cmp(customer.password, password):
        return customer


def identity(payload):
    _id = payload['identity']
    return CustomerModel.find_by_id(_id)