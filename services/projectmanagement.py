from flask import Flask, render_template
 

app = Flask(__name__)

headings = ("Task","Task Assigned","Task Status")
data = (
    ("Estimate budget", "Timothy McCreesh", "Completed"),
    ("Web page designs", "Enci Zou", "In Progress"),
    ("Project Documentation", "Daniel Chao", "In Progress"),
    ("Program web pages", "Druvil Patel", "In Progress"),
)

@app.route("/")
def home():
    
    return render_template('tasktable.html')