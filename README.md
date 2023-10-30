# test_api
Resolve errors in Flask-Pydantic

* Create a python environment using.
```bash
python3 -m venv venv 
```

* Activate the environement

```bash
source ./venv/bin/activate
```

`source venv/bin/activate`

* Install requirements

```bash
pip install flask \
            pydantic \
            flask_pydantic \
            flask_restful
```

* Also install any other packages if required.

* To run

```bash
 python3 main.py
```

* Access the endpoint
```
http://localhost:5000?age=10
```
This get request will produce an error and it can be seen in ![here]("issue_attrubute_error_on_pydantic_query.png") 
