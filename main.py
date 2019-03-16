import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from domains import Post

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # db.create_all()
    files = os.listdir('CS')
    files = ['CS/' + file for file in files ]
    file = files[0]
    with open(file) as f:
        message = [ { line.strip().rsplit(":")[1] : line.strip().rsplit(":")[2]} for line in f.readlines()[1:-1]]
        print(message)
    # app.run()