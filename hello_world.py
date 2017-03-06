from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
     return render_template('template.html', my_string="Hello World!",) 
    
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html', my_string="Hello "+name.title()+"!",)
    
@app.route("/jedi/<name1>/<name2>")
def jedi(name1,name2):
    a = name1[:2]
    b = name2[:3]
    return render_template('template.html', my_string="Jedi "+b.title()+a,) 


if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))