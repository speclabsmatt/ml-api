from flask import Flask, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    from .models import Entry
    main_entry = Entry.query.order_by(Entry.id).first()
    print(main_entry)
    return jsonify(main_entry.data)


DB_URI = app.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(DB_URI)
