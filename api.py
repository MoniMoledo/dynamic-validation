from flask import Flask, request
import json
from flask_restful import Resource, Api, abort
from validator import CustomerValidator

app = Flask(__name__)
api = Api(app)
validator = CustomerValidator()


class CustomerValidation(Resource):
    @staticmethod
    def internal_server_error(message):
        response = {"message": message}
        response["status_code"] = 500
        return response

    def get(self):
        try:
            url = 'https://backend--winter-2017.herokuapp.com/customers.json'
            invalid_customers = []
            response = {}

            data = validator.get_api_response(url, 1)
            number_of_pages = validator.get_api_number_of_pages(data)
            for page in range(1, number_of_pages + 1):

                data = validator.get_api_response(url, page)

                customers, validations = validator.get_customers_and_validations(data)
                validation_result = validator.get_customer_validation(customers, validations)

                invalid_customers.extend(validation_result)

            response["invalid_customers"] = invalid_customers

            return response
        except Exception as e:
            return self.internal_server_error(e.message)


api.add_resource(CustomerValidation, '/invalid_customers')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000)

