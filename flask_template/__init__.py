from flask import Flask, render_template

app = Flask(__name__)

from flask_template.a_route.routes import a_route
from flask_template.main.routes import main

app.register_blueprint(a_route)
app.register_blueprint(main)


if __name__ == '__main__':
    app.run()