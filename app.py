from flask import Flask
from APIs.Auth import auth_api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
app.register_blueprint(auth_api)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

if __name__ == '__main__':
    app.run(port=5000)
