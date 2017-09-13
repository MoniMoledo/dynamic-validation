from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class CustomerValidation(Resource):
    def get(self):
        url = ""
        invalid_customers = []
        response = {}
        response["invalid_customers"] = invalid_customers

        return response

api.add_resource(CustomerValidation, '/invalid_customers')

if __name__ == '__main__':
    app.run()
