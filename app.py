from flask import Flask, Blueprint, render_template
from flask_cors import CORS


# live API
from api.restplus import api as api
#from api.unidade.endpoints import ns as unidade_namespace
#from api.subunidade.endpoints import ns as subunidade_namespace
from api.docente.endpoints import ns as docente_namespace
#from api.curso.endpoints import ns as curso_namespace
#from api.biblioteca.endpoints import ns as biblioteca_namespace


import settings


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    CORS(flask_app)


blueprint = Blueprint('api', __name__, url_prefix='/api/v01')
api.init_app(blueprint)



app = Flask(__name__)
configure_app(app)

app.register_blueprint(blueprint)


# Endpoint Home
# Endpoint Home
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__': 
    app.run(debug=True)
