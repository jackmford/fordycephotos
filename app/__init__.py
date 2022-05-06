import os

from flask import Flask
from app import cleanphotos

def create_app():
    app = Flask(__name__)

    app.register_blueprint(cleanphotos.bp)

    return app
