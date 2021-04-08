#app.py
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/employeeprofile'
app.config['SECRET_KEY'] = "random string"
 
db = SQLAlchemy(app)
 
 
#Creating model table for our employee profile database
class employeeprofile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone


@app.route('/')
def show_all():
    return render_template('show_all.html',employeeprofile = employeeprofile.query.all())


#This route is for adding info for our employee
@app.route('/new/', methods = ['GET', 'POST'])
def new():
    if request.method== 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['phone']:flash('Please enter all the fields','error')
        else:
            employee = employeeprofile(request.form['name'],request.form['email'],request.form['phone'])
            print(employee)
            db.session.add(employee)
            db.session.commit()
            flash('Record was sucessfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=False)
