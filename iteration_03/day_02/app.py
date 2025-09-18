from flask import Flask, render_template
from user import User
from random import choice
import json

app = Flask(__name__)

sample_users = [
    {"name": "Alex", "age": 47, "hobby": "hiking"},
    {"name": "Lorcan", "age": 18, "hobby": "calisthenics"},
    {"name": "Sophia", "age": 24, "hobby": "yoga"},
    {"name": "Siddiqi", "age": 17, "hobby": "running"},
    {"name": "Amir", "age": 60, "hobby": "reading"},
    {"name": "Steven", "age": 33, "hobby": "freelancing"},
    {"name": "Artiom", "age": 10, "hobby": "eating"},
    {"name": "Emily", "age": 45, "hobby": "biking"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
def user():
    random_user = choice(sample_users)
    user = User(random_user["name"], random_user["age"], random_user["hobby"])

    try:
        with open('users.json', 'r') as f:
            user_list = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        user_list = []

    user_list.append(random_user)

    with open('users.json', 'w') as f:
        json.dump(user_list, f, indent=4, sort_keys=True)

    return render_template('user.html', user=user)

@app.route('/saved-users')
def saved_users():
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        users = []
    return render_template('saved_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)