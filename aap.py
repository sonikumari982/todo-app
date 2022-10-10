from crypt import methods
import string
from turtle import title
from flask import flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


aap=flask(_name_)
aap.config['SQLALCHENY_DATABASE_URL']='sqlite:///database.db'
aap.config['SQLALCHENY_TRACK_MODIFICATION']= False
db =SQLAlchemy(app)

class todo(db.model):
    title=db.column(db.string(200), primary_key=True)
    desc=db.column(db.string(300),nullable=False)

    def __repr__(self) -> str:
        return f"{self.title} - {self.desc}"


@app.route('/')
def helloworld():
    return render_template("index.html")


@app.routed('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        title = request.from ["title"]
        desc = request.from ["desc"]
        todo = Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template("add.html",alltodo = alltodo)

if _name_ == "_main_":
    app.run(debug=True)