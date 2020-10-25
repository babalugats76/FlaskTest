from flask import Flask
from flask_cors import CORS
import os
import logging
app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {"origins": ["https://cdpn.io"]}})
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('flask_cors').level = logging.DEBUG
app.config['AUTHOR'] = os.environ.get('AUTHOR', None)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', None)
from todo import controllers