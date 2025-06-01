from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)


@contacts.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@contacts.route('/new', methods=['POST'])
def add_contact():
    return "<h1>saving contact</h1>"


@contacts.route('/update', methods=['POST'])
def update():
    return "<h1>update contact</h1>"


@contacts.route('/delete', methods=['POST'])
def delete():
    return "<h1>delete contact</h1>"


@contacts.route('/about', methods=["GET"])
def about():
    return render_template('about.html')
