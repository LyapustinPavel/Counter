
from flask import Flask
from config import Config

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
app.config.from_object(Config)
from app import route