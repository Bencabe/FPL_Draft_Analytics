from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'fantasy_football'

mysql = MySQL(app)
# cur = mysql.connection.cursor()
# cur.execute('''SELECT* FROM weekly_player_score''')
# res = cur.fetchall()


# def leaders_per_week(result):
#     # function to return leader each week
#     leader = []
#     teams = []
#     for row in result:
#         print("yes")
#     return "placeholder"


@app.route('/', methods=['GET', 'POST'])

def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT* FROM weekly_player_score''')
    res = cur.fetchall()
    return render_template('index.html',all_info=res)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)