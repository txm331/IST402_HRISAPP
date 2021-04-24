from flask import Flask, jsonify, make_response, render_template
import json
import os
import simplejson as json
#accounting
app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/static/sales.json".format(database_path), "r") as f:
    sale = json.load(f)

@app.route('/', methods=['GET'])
def hello():
    ''' Greet the user '''

    return render_template("layout.html")

@app.route('/sales', methods=['GET'])
def sales():
    ''' Displays all the lists '''
    resp = make_response(json.dumps(sale, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return render_template("sales.html")

@app.route('/sales/<username>', methods=['GET'])
def sales_data(username):
    ''' Returns info about a specific user '''

    if username not in sale:
        return "Not found"

    return jsonify(sale[username])

@app.route('/sales/<username>/lists', methods=['GET'])
def sales_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://127.0.0.1:5004{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text

if __name__ == '__main__':
    app.run(port=5004, debug=True)
