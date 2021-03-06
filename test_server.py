from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'fantasy_football'

mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])

def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT* FROM weekly_player_score''')
    player_scores = cur.fetchall()
    cur.execute('''SELECT* FROM fixtures ORDER BY gameweek''')
    fixtures = cur.fetchall()
    return render_template('index.html',scores_info=player_scores,fixtures=fixtures)

@app.route('/weekly_leaders', methods=['GET', 'POST'])

def weekly_leaders():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT* FROM weekly_player_score''')
    player_scores = cur.fetchall()
    cur.execute('''SELECT* FROM fixtures ORDER BY gameweek''')
    fixtures = cur.fetchall()
    return render_template('weekly_leaders.html',scores_info=player_scores,fixtures=fixtures)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)