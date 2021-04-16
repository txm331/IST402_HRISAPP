from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route("/it/")
def it():
    return render_template("it.html", headings=headings, data=data)

headings = ("Employee#","Name","Entry Year","Age","Department")
data = (
    ("23434","Catherine Della","2010","45","IT"),
    ("34343","Egbert Well","2010","27","IT"), 
    ("23145","David Coolman","2010","29","IT"),
    ("78455","Andy Apple","2011","35","IT"), 
    ("45245","Anna Dish","2012","24","IT"),
)