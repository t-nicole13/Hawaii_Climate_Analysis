from flask import Flask

# create a new app instance
app = Flask(__name__)

# create flask routes
@app.route('/')
def hello_world ():
    return 'Hello World'

# run a flask app in terminal



