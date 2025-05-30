from flask import blueprints, render_template

index_blueprint = blueprints.Blueprint('index', __name__, url_prefix="/")

@index_blueprint.route('/')
def index():
    return render_template('index.html')