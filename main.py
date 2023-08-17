from flask_sqlalchemy import SQLAlchemy
from website import create_app
from flask import Flask

app = create_app()
app= Flask(__name__)

app.static_url_path = '/static'

if __name__=='__main__':
    app.run(debug=True)

db = SQLAlchemy()
