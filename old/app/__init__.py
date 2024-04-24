from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os 

file_path = os.path.abspath(os.getcwd())+"/scores.db"

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path 
db = SQLAlchemy(app)

from app import routes

if __name__ == '__main__': 
    db.create_all()
    app.run(debug=False)
