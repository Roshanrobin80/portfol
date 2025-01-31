import sqlite3
from flask import Flask, render_template,request

con = sqlite3.connect("dbs.db")
try:
    con.execute("create table msg(name text,email email,msg text)")
except sqlite3.OperationalError:
    pass

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/contact',methods=['GET','POST'])


def contact():
    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        msg=request.form.get('msg')
        print(name,email,msg)
        con=sqlite3.connect('dbs.db')
        con.execute("insert into msg(name,email,msg)values(?,?,?)",(name,email,msg))
        con.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)