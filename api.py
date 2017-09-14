from flask import Flask, request
from flask_restful import Resource, Api
from validator import CustomerValidator

app = Flask(__name__)
api = Api(app)
validator = CustomerValidator()


class CustomerValidation(Resource):
    def get(self):
        url = 'https://backend-challenge-winter-2017.herokuapp.com/customers.json'
        invalid_customers = []
        response = {}

        number_of_pages = validator.get_api_number_of_pages(url)
        for page in range(1, number_of_pages + 1):

            customers, validations = validator.get_customers_and_validations(url, page)

            validation_result = validator.get_customer_validation(customers, validations)

            invalid_customers.extend(validation_result)

        response["invalid_customers"] = invalid_customers

        return response

api.add_resource(CustomerValidation, '/invalid_customers')

if __name__ == '__main__':
    app.run()
