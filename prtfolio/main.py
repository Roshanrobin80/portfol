from flask import Flask,render_template,request
import sqlite3
con=sqlite3.connect("/home/novavi/Documents/roshan/flask/dbs.db")
try:
    con.execute("create table std(name text,age int,email email)")
except:
    pass
set FLASK_APP=main.py
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('htm.html')
