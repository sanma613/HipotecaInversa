from flask import Flask
import sys
sys.path.append("src")

from controller.routes.index import index_blueprint
from controller.routes.buscar import buscar_blueprint
from controller.routes.admin import admin_blueprint
from controller.routes.ver_todos import ver_todos_blueprint
from controller.routes.insertar_todos import insertar_todos_blueprint

app = Flask(__name__, template_folder='src/view/web/templates', static_folder='src/view/web/static')
app.secret_key = 'secret_key'
app.register_blueprint(index_blueprint)
app.register_blueprint(buscar_blueprint)
app.register_blueprint(insertar_todos_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(ver_todos_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)