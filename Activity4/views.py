from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/blog")
def blog():
    return render_template("blog.html")

@views.route("/contacts")
def contacts():
    return render_template("contacts.html")
