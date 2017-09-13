import requests
import math
import json
from schema_specs import Schema


class CustomerValidator:

    def get_api_number_of_pages(self, url):
        response = requests.get(url=url)
        data = response.json()

        number_of_customers = float(data["pagination"]["total"])
        customers_per_page = float(data["pagination"]["per_page"])
        float_number_of_pages = number_of_customers/customers_per_page
        number_of_pages = int(math.ceil(float_number_of_pages))

        return number_of_pages

    def get_customers_and_validations(self, url, page):
        params = dict(page=page)
        response = requests.get(url=url, params=params).json()
        
        return response["customers"], response["validations"]

    def get_customer_validation(self, customers, validations):
        invalid_customers = []
        schema = Schema()
        
        self.schema.create(validations)

        for customer in customers:
            validation_result = self.json_schema.validate(customer)
            if(any(validation_result)):
                invalid_customers.append(validation_result)
        return invalid_customers
