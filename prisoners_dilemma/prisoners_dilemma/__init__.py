from flask import Flask
from flask import request, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
