import os
import json
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['DEBUG'] = os.environ.get('DEBUG', False)
db = SQLAlchemy(app)

class Game(db.Model):
    __tablename__  = 'games'
    id = db.Column(db.Integer, primary_key=True)
    provider_game_id = db.Column(db.String(255), unique=True)
    provider_game_name = db.Column(db.String(255))
    provider_game_category = db.Column(db.String(255))

    def get(self, attr, default):
        return getattr(self, attr, default)

    def __repr__(self):
        return '<Game {}, {}, {}, {}>'.format(self.id,
                                              self.get('provider_game_id',
                                                       None),
                                              self.get('provider_game_name',
                                                       None),
                                              self.get('provider_game_category',
                                                       None)
                                              )
    def __str__(self):
        return self.__repr__()

@app.route('/')
def games():
    return jsonify({'games':[str(g) for g in Game.query.all()]})

if __name__ == "__main__":
    app.run(port=5040, debug=True)
