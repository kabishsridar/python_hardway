from flask import Flask # Importing modules
from flask import render_template
from flask import request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"

        con = sql.connect('kabish.db') # connecting to database
        cur = con.cursor() # creating a cursor instance
        cur.execute('''CREATE TABLE IF NOT EXISTS INFO (
                        GREETING TEXT NOT NULL,
                        USER_NAME TEXT NOT NULL)''') # creates a table if does not exists
        cur.execute('INSERT INTO INFO (GREETING, USER_NAME) VALUES (?, ?)', (greet, name)) # inserts the values to the table
        con.commit() # commits the changes to the database
        cur.execute('SELECT * FROM INFO;')
        information = cur.fetchall()
        
        cur.close() # closes the connection and cursor instance
        con.close()

        return render_template("display_names.html", information=information0)

        return render_template("index.html", greeting=greeting) # calls the index file
    else:
        return render_template("hello_form.html") # calls the hello_form file

if __name__ == "__main__":
    app.run(debug=True) # calling the function to execute
