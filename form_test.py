from flask import Flask # Importing modules
from flask import render_template
from flask import request
import sqlite3 as sql

app = Flask(__name__)

con = sql.connect('kabish.db') # connecting to database
cur = con.cursor() # creating a cursor instance
cur.execute('''CREATE TABLE IF NOT EXISTS INFO (
                GREETING TEXT NOT NULL,
                USER_NAME TEXT NOT NULL)''') # creates a table if does not exists

@app.route("/hello", methods=['POST', 'GET'])
def index(): # defining a function index
    print(request.form) # displays the request object
    con = sql.connect('kabish.db') # connecting to the database
    cur = con.cursor() # creating a cursor instance
    name = request.form['name'] # getting name and greet from the request for
    greet = request.form['greet']
    greeting = f"{greet}, {name}"

    cur.execute('INSERT INTO INFO (GREETING, USER_NAME) VALUES (?, ?)', (greet, name)) # inserts the values to the table
    con.commit() # commits the changes to the database
    con.close()
    return render_template("index.html", greeting=greeting) # calls the index file

@app.route('/display', methods=['GET'])
def display():
    con = sql.connect('kabish.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM INFO;')
    information = cur.fetchall()
    con.close()
    return render_template("display_names.html", information=information)

@app.route('/getinput', methods=['GET'])
def test():
    return render_template("hello_form.html") # calls the hello_form file

if __name__ == "__main__":
    app.run(debug=True) # calling the function to execute