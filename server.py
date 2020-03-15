from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@127.0.0.1:3306/fantasy_football'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# instantiating db instance
db = SQLAlchemy(app)

class Weekly_player_scores(db.Model):
    # declare table name
    __tablename__ = 'weekly_player_scores'
    # define columns in table
    player_name = db.Column('player_name', db.Unicode, primary_key=True)

all_info = Weekly_player_scores.query.all()

player_names = []

for el in all_info:
    player_names.append(el.player_name)

df = pd.DataFrame()

df['player_names'] = player_names

json_string = df.to_json()
json_object = json.loads(json_string)

@app.route('/')
def root():
    # rendering index.html and passing in player info
    return render_template('index.html', all_info=json_object)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
