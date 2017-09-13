import json
from jsonschema import Draft4Validator
from type import Type


class Schema:

    schema = {}

    def __init__(self):
        schema = {}

    def build(self, properties, required_properties):
        self.schema = {
            "type": "object",
            "properties": properties,
            "required": required_properties,
        }

    def get_length_requirements(self, validation, field_name):
        max_len = validation[field_name].get("length", {}).get("max", None)
        min_len = validation[field_name].get("length", {}).get("min", None)
        return max_len, min_len

    def create(self, validations):
        required_properties = []
        properties = {}

        for validation in validations:
            type_object = Type()
            field_name = validation.keys()[0]

            required_type = validation[field_name].get("type", "default")
            type_object.set_supported_type(required_type)

            if(validation[field_name].get("required", False)):
                required_properties.append(field_name)

            is_required = field_name in required_properties
            type_object.set_optional_type(is_required)

            max_len, min_len = self.get_length_requirements(validation, field_name)
            type_object.set_lenght_requirements(max_len, min_len)

            properties[field_name] = type_object.get_type_requirements()

        self.build(properties, required_properties)

    def validate(self, instance):
        response = {}
        invalid_fields = []
        v = Draft4Validator(self.schema)
        for e in sorted(v.iter_errors(instance), key=str):
            response['id'] = instance["id"]
            for error_field in e.path:
                invalid_fields.append(error_field)
            response['invalid_fields'] = invalid_fields
        return response
