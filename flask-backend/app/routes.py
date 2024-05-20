from flask import Flask, jsonify
from models import User, Work1, About1, Contact, Category, Register, Services

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the API"})

@app.route('/about1')
def about1():
    data = {
        "title": "About1",
        "content": "This is the about1 page."
    }
    return jsonify(data)

@app.route('/work1')
def work1():   
    data = {
        "title": "Work1",
        "content": "This is the work1 page."
    }
    return jsonify(data)

@app.route('/category')
def category():
    data = {
        "title": "Category",
        "content": "This is the category page."
    }
    return jsonify(data)

@app.route("/api/register")
def get_register():
    register = Services.query.all()
    return jsonify([register.to_dict() for register in register])


@app.route('/contact')
def contact():
    data = {
        "title": "Contact",
        "content": "This is the contact page."
    }
    return jsonify(data)

@app.route('/experience')
def experience():
    data = {
        "title": "Experience",
        "content": "This is the experience page."
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
