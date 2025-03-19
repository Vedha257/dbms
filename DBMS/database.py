from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config  # Import database credentials

app = Flask(__name__)

# Configure Flask to use the database
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Connect to MySQL and create the database if it doesn’t exist
connection = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD)
cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME};")
cursor.close()
connection.close()

print("✅ Database connected successfully!")
