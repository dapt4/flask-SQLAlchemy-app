from flask import Flask
from utils.db import DB_URL, db

from routes.contacts import contacts

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy(app) # no es necesario hacer dos instancias
db.init_app(app)

app.register_blueprint(contacts)
