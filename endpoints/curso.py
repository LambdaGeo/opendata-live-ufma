from flask_restplus import Resource
from restplus import api as liveapi
from ufma_scrapper import curso


ns = liveapi.namespace('curso', description='Operations related to "curso"')


@ns.route('/')
class Curso(Resource):
    def get(self):
        return curso.get_cursos()


@ns.route('/<string:codigo>/monografias/<string:ano>')
class Monografias(Resource):
    def get(self, codigo, ano):
        return curso.get_monografias(codigo, ano)


@ns.route('/<string:codigo>/discentes')
class Discentes(Resource):
    def get(self, codigo):
        return curso.get_discentes_ativos(codigo)


@ns.route('/<string:codigo>/turmas/<string:ano>/<string:periodo>')
class Turmas (Resource):
    def get(self, codigo, ano, periodo):
        return curso.get_turmas(codigo, ano, periodo)
