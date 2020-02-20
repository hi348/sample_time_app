from flask import Flask
app = Flask(__name__)

import datetime as timmy
from pytz import timezone

@app.route('/')
def hello_world():
    return 'You were the Chosen One!!!'
	
@app.route('/time')
def timm():
    return  timmy.datetime.now(timezone('UTC')).astimezone(timezone('US/Eastern')).strftime("%H:%M")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
