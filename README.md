# dynamic-validation

Python API to validate an instance based on a given specification of the instance fields.

## Getting Started

To run API:

```
python api.py
```

Then request API:
 
```
GET localhost:8000/invalid_customers
```

### Prerequisites

Python 2.7

Modules:

- flask
- flask-restful
- jsonschema


### Installing

First step install dependencies:

```
pip install flask
```

```
pip install flask-restful
```

```
pip install jsonschema 
```

Then you can call the API.

Response example:

```json
{
"invalid_customers": [
    { "id": 1, "invalid_fields": ["name", "age"] },
    { "id": 3, "invalid_fields": ["password"] }
  ]
}
```