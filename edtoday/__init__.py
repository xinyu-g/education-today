from flask import Flask 
from flask.ext.mysql import MySQL
from api import main


db = MySQL()

def create_app():
    app = Flask(__name__)

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'eductoday'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    
    db.init_app(app)
    
    app.register_blueprint(main)

    return app