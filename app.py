import os

from flask import Flask, render_template
from api_v1 import api as api_v1

from models import db

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def hello():
    return 'Hello world!'


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test1234@localhost/board'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ThisIsMySecretKey'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
