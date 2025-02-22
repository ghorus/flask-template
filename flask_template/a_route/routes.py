from flask import render_template, Blueprint

a_route = Blueprint('a_route',__name__)

@a_route.route("/a_route")
def index():
    return render_template("a_route/index.html")