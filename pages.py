from flask import Blueprint, render_template, redirect, url_for, request
pages = Blueprint("pages", __name__, static_folder="static", template_folder="templates")

@pages.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("pages.user", usr=user))
    else:
        return render_template("index.html")
@pages.route("/<usr>")
def user(usr):
    return render_template("not found.html")

@pages.route("/notfound")
def notfound():
    return render_template("not found.html")

@pages.route("/GDT")
def victims():
    return render_template("victims.html")

@pages.route("/GDT/1")
def one():
    return render_template("/GDT/1.html")

