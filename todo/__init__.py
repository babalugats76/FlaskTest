from flask import Flask
from flask_cors import CORS
import logging
app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {"origins": ["https://cdpn.io"]}})
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('flask_cors').level = logging.DEBUG
from app import controllers