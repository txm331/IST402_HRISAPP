from flask import Flask, jsonify, make_response
import json
import os
import simplejson as json
#marketing
app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/static/marketing.json".format(database_path), "r") as f:
    acc = json.load(f)

@app.route('/', methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hey! The service is up, how about doing something useful"

@app.route('/marketing', methods=['GET'])
def marketing():
    ''' Displays all the lists '''
    resp = make_response(json.dumps(acc, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp

@app.route('/marketing/<username>', methods=['GET'])
def marketing_data(username):
    ''' Returns info about a specific user '''

    if username not in acc:
        return "Not found"

    return jsonify(acc[username])

@app.route('/marketing/<username>/lists', methods=['GET'])
def marketing_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://127.0.0.1:5001/lists/{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text

if __name__ == '__main__':
    app.run(port=5005, debug=True)
