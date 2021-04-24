from flask import Flask, jsonify, make_response, render_template
import json
import os
import simplejson as json
#projectmanagement
app = Flask(__name__)
#Testing!!!
database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/static/projectmanagement.json".format(database_path), "r") as f:
    acc = json.load(f)

@app.route("/")
def hello():
    ''' Greet the user '''

    return render_template("tasktable.html")

@app.route('/projectmanagement', methods=['GET'])
def projectmangement():
    ''' Displays all the lists '''
    resp = make_response(json.dumps(acc, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return render_template("projectmanagement.html")

@app.route('/projectmanagement/<username>', methods=['GET'])
def projectmangement_data(username):
    ''' Returns info about a specific user '''

    if username not in acc:
        return "Not found"

    return jsonify(acc[username])

@app.route('/projectmanagement/<username>/lists', methods=['GET'])
def projectmangement_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://127.0.0.1:5001/lists/{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text


@app.route("/")
def tasktable():
    return render_template("tasktable.html")

if __name__ == '__main__':
    app.run(port=5003, debug=True)
