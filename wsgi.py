
import imp
from flask import Flask
from markupsafe import escape
from flask import render_template
from requests import request

app = Flask(__name__)


@app.route('/')
def loadout():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("SOMETHING ELSE")
        elif request.form['submit_button'] == 'Do Something Else':
            print("SOMETHING ELSE")
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('loadout.html')


@app.route('/start_car/')
def start_car():
    ###########
    print("YEAAAAAAAAAAAAAAAAAAAAAAA")
    return 'Starting'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

print('DONE')
