from flask import Blueprint, redirect, render_template, request

from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)


@contacts.route('/', methods=["GET"])
def home():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])
def add_contact():
    try:
        username, email, phone = request.form.values()
        contact = Contact(username, email, phone)
        db.session.add(contact)
        db.session.commit()
        return redirect('/')
    except Exception:
        return redirect('/', 501)


@contacts.route('/update', methods=['POST'])
def update():
    return "<h1>update contact</h1>"


@contacts.route('/delete', methods=['POST'])
def delete():
    return "<h1>delete contact</h1>"


@contacts.route('/about', methods=["GET"])
def about():
    return render_template('about.html')
