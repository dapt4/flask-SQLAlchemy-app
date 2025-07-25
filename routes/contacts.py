from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, url_for)

from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)


@contacts.route('/', methods=["GET"])
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])
def add_contact():
    try:
        fullname, email, phone = request.form.values()
        contact = Contact(fullname, email, phone)
        db.session.add(contact)
        db.session.commit()
        flash('Contact added successfully!')
        return redirect(url_for('contacts.index'))
    except Exception:
        return redirect(url_for('contacts.index'), 501)


@contacts.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    contact = Contact.query.get(id)
    if not contact:
        return "Contacto no encontrado", 404
    if request.method == "GET":
        contact = Contact.query.get(id)
        return render_template('update.html', contact=contact)
    else:
        fullname, email, phone = request.form.values()
        contact.fullname = fullname
        contact.email = email
        contact.phone = phone
        db.session.commit()
        flash('Contact updated successfully!')
        return redirect(url_for('contacts.index'))


@contacts.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!')
    return redirect(url_for('contacts.index'))


@contacts.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


@contacts.route('/test', methods=["POST"])
def test():
    data = request.get_json()
    nombre = data.get('nombre')
    edad = data.get('edad')
    print([nombre, edad])
    return jsonify(data)
