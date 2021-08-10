from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return "Dagbok API"


DB_URI = app.config['SQLALCHEMY_DATABASE_URI']
# engine = create_engine(DB_URI)
