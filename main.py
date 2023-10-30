# vanilla flask api using pydantic

# from flask import Flask, request, jsonify
# from pydantic import BaseModel
#
# from flask_pydantic import validate
#
#
# app = Flask(__name__)
#
# # Define a Pydantic model for query parameters
# class ItemQueryParams(BaseModel):
#     min_price: float = None
#     max_price: float = None
#
# # Define a simple route
# @app.route('/items', methods=['GET'])
# @validate()
# def get_items(query: ItemQueryParams):
#     min_price = query.min_price
#     max_price = query.max_price
#
#     items = [
#         {'name': 'item1', 'price': 10.99},
#         {'name': 'item2', 'price': 5.99},
#         {'name': 'item3', 'price': 7.50}
#     ]
#
#     if min_price is not None:
#         items = [item for item in items if item['price'] >= min_price]
#
#     if max_price is not None:
#         items = [item for item in items if item['price'] <= max_price]
#
#     return jsonify(items)
#
# if __name__ == '__main__':
#     app.run(debug=True)


from typing import Optional
from flask import Flask, request
from pydantic import BaseModel

from flask_pydantic import validate

app = Flask("flask_pydantic_app")

class QueryModel(BaseModel):
  age: int

class ResponseModel(BaseModel):
  id: int
  age: int
  name: str
  nickname: Optional[str]

# Example 1: query parameters only
@app.route("/", methods=["GET"])
@validate()
def get(query: QueryModel):
  age = query.age
  return ResponseModel(
    age=age,
    id=0, name="abc", nickname="123"
    )


if __name__ == '__main__':
    app.run(debug=True)


