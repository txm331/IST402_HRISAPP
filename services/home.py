from flask import Flask, jsonify, make_response, render_template
import json
import os
import simplejson as json
#home
app = Flask(__name__)
#Testing!!!


@app.route("/")
def hello():
    ''' Greet the user '''

    return render_template("layout.html")



@app.route("/")
def tasktable():
    return render_template("tasktable.html")

if __name__ == '__main__':
    app.run(port=5004, debug=True)
