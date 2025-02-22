from flask import Flask, render_template

app = Flask(__name__)

from flask_template.a_route.routes import a_route
app.register_blueprint(a_route)

@app.route('/')
def index():
    message = "Hi"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()