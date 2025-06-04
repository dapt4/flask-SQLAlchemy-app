from app import app
from utils.db import db
import os

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    os.system('sh run.sh')
