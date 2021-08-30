from flask import Flask
from APIs.Auth import auth_api
from core import limiter


app = Flask(__name__)
limiter.init_app(app)
app.register_blueprint(auth_api)


if __name__ == '__main__':
    app.run(port=5000)
