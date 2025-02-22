from livereload import Server
from flask_template import app

app.debug = True
server = Server(app.wsgi_app)

server.watch("flask_template/templates")
server.watch("flask_template/static")
server.serve()