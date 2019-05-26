from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def hello1():

    return render_template("index.htm")
app.run(debug = True)