import sqlite3
from flask import Flask, render_template

con = sqlite3.connect("c:/Users/My Pc/OneDrive/Documents/roshan/portfol/prtfolio/dbs.db")
try:
    con.execute("create table std(name text, age int, email text)")
except sqlite3.OperationalError:
    pass

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

