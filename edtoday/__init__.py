from flask import Flask 
from flaskext.mysql import MySQL



db = MySQL()

def create_app():
    app = Flask(__name__)

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'eductoday'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    
    db.init_app(app)

    from .api import main
    app.register_blueprint(main)

    return app