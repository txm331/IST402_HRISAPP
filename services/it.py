from flask import Flask, jsonify, make_response,render_template
import json
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/static/it.json".format(database_path), "r") as f:
    usr = json.load(f)

@app.route('/', methods=['GET'])
def hello():
  return render_template('layout.html')

@app.route('/it', methods=['GET'])
def it():
    ''' Displays all the lists '''
    resp = make_response(json.dumps(usr, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return render_template('it.html')

@app.route('/it/<username>', methods=['GET'])
def it_data(username):
    ''' Returns info about a specific user '''

    if username not in usr:
        return "Not found"

    return jsonify(usr[username])

@app.route('/it/<username>/lists', methods=['GET'])
def it_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://127.0.0.1:5002/lists/{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text

if __name__ == '__main__':
    app.run(port=5002, debug=True)