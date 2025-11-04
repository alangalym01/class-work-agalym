from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

data = {
    "info": {
        "name":"Alan",
        "age":18,
        "phone":"123-456-7890",
        "email":"trash@email.com",
        "hometown":"Brooklyn, NYC"
    },
    "interest": "Python",
    "skills": [
        "Flask",
        "Django",
        "React JS",
    ],
}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template("contact.html", info=data["info"])

@app.route("/about")
def about():
    return render_template("about.html", info=data["info"], interest=data["interest"], skills=data["skills"])

if __name__ == "__main__":
    app.run(debug=True)