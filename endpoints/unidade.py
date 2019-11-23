from flask_restplus import Resource, fields
from restplus import api as api
from ufma_scrapper import unidade
import json

ns = api.namespace('unidade', description='Operations related to "unidade"')


with open('endpoints/unidades.json') as json_file:  
    unidades = json.load(json_file)

unidades_field = api.model('Unidade' ,{
    'nome': fields.String,
    'diretor': fields.String,
    'telefone': fields.String,
    'end_alt': fields.String
})


@ns.route('/')
class Unidade (Resource):
    def get(self):
        return unidades


@ns.route('/<string:codigo>')
class Unidade (Resource):
    @api.marshal_with(unidades_field)
    def get(self, codigo):
        return unidade.get_unidade(codigo)


@ns.route('/<string:codigo>/subunidade')
class Subunidades(Resource):
    def get(self, codigo):
        return unidade.get_subunidades(codigo)


@ns.route('/<string:codigo>/grupos_pesquisa')
class Grupos_Pesquisa(Resource):
    def get(self, codigo):
        return unidade.get_grupos_pesquisa(codigo)


@ns.route('/<string:codigo>/cursos_pos')
class Cursos_Pos(Resource):
    def get(self, codigo):
        return unidade.get_cursos_pos(codigo)


@ns.route('/<string:codigo>/cursos_graduacao')
class Cursos_Graduacao(Resource):
    def get(self, codigo):
        return unidade.get_cursos_graduacao(codigo)