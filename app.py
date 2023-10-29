from flask import Flask, request
from flask_restful import Api, Resource
from pydantic import BaseModel

app = Flask(__name__)
api = Api(app)

# Define a Pydantic model for query parameters
class ItemQueryParams(BaseModel):
    min_price: float = None
    max_price: float = None

# Define a simple resource
class ItemList(Resource):
    def get(self):
        params = ItemQueryParams(**request.args)
        min_price = params.min_price
        max_price = params.max_price

        items = [
            {'name': 'item1', 'price': 10.99},
            {'name': 'item2', 'price': 5.99},
            {'name': 'item3', 'price': 7.50}
        ]

        if min_price is not None:
            items = [item for item in items if item['price'] >= min_price]

        if max_price is not None:
            items = [item for item in items if item['price'] <= max_price]

        return items

# Add the resource to the API with a specific URL endpoint
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)

