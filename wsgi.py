
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/')
def loadout():
    return render_template('loadout.html')


@app.route('/start_car/')
def start_car():
    ###########
    print("YEAAAAAAAAAAAAAAAAAAAAAAA")
    return 'Starting'


print('DONE')
