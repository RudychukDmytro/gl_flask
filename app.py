import os

from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
database_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database/app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.String(50), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vote', methods=['POST'])
def proces_vote():
    vote_value = request.form['vote']
    new_vote = Vote(vote=vote_value)
    db.session.add(new_vote)
    db.session.commit()
    return 'Голос збережено!'


if __name__ == '__main__':
    app.run(debug=True)
