from flask import Flask
from flask import render_template # it takes the file from templates folder by default
# render_template is used to render HTML templates

app = Flask(__name__) # __name__ is the name of the current module, it is used to determine the root path of the application

@app.route('/') # this is the root URL of the application
def index():
    greeting = "Hello World"
    return render_template('index.html', greeting=greeting) # render_template takes the name of the HTML file and any variables to pass to the template
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables the debug mode, which will automatically reload the server when changes are made to the code
    