from flask import Flask, Blueprint, render_template
from flask_cors import CORS
from restplus import api as api
from endpoints.unidade import ns as unidade_namespace
from endpoints.subunidade import ns as subunidade_namespace
from endpoints.docente import ns as docente_namespace
from endpoints.curso import ns as curso_namespace
from endpoints.biblioteca import ns as biblioteca_namespace
import settings
import os

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


api.add_namespace(unidade_namespace)
api.add_namespace(subunidade_namespace)
api.add_namespace(docente_namespace)
api.add_namespace(curso_namespace)
api.add_namespace(biblioteca_namespace)



app = Flask(__name__)
configure_app(app)


app.register_blueprint(blueprint)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__': 
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 
