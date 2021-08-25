import os
from flask import Flask
from APIs.Auth import auth_api

app = Flask(__name__)
app.register_blueprint(auth_api)

@app.route('/')
def home():
    return '<h1>Welcome to the Home Page. Application is Under construction.</h1>'


if __name__ == '__main__':

    app.run(port=5000)
