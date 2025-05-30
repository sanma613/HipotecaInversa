from flask import Flask
import sys
sys.path.append("src")

from view.web.routes.index import index_blueprint
from view.web.routes.buscar import buscar_blueprint
from view.web.routes.admin import admin_blueprint
from view.web.routes.ver_todos import ver_todos_blueprint
from view.web.routes.insertar_todos import insertar_todos_blueprint
from view.web.routes.eliminar1 import eliminar_blueprint
from view.web.routes.hipoteca_inversa import hipoteca_blueprint

app = Flask(__name__, template_folder='src/view/web/templates', static_folder='src/view/web/static')
app.secret_key = 'secret_key'
app.register_blueprint(index_blueprint)
app.register_blueprint(buscar_blueprint)
app.register_blueprint(insertar_todos_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(ver_todos_blueprint)
app.register_blueprint(eliminar_blueprint)
app.register_blueprint(hipoteca_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)