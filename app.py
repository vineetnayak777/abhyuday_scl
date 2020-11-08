from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("layout.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/listen")
def listen():
    return render_template("listen.html")

@app.route("/student")
def student():
    return render_template("student.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__=='__main__':
    app.run(host='localhost',port=3000,debug=True)