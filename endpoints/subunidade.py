from flask_restplus import Resource
from restplus import api as api
from ufma_scrapper import subunidade

ns = api.namespace('subunidade', description='Operations related to "subunidade"')


@ns.route('/')
class SubUnidade (Resource):
    def get(self, ):
        return subunidade.get_subunidades()


@ns.route('/<string:codigo>')
class SubUnidade (Resource):
    def get(self, codigo):
        return subunidade.get_subunidade(codigo)


@ns.route('/<string:codigo>/disciplina')
class Disciplinas(Resource):
    def get(self, codigo):
        return subunidade.get_disciplinas(codigo)


@ns.route('/<string:codigo>/docente')
class Docentes(Resource):
    def get(self, codigo):
        return subunidade.get_docentes(codigo)


'''
@ns.route('/<string:codigo>/administrativo')
class Administrativo(Resource):
    def get(self, codigo):
        return subunidade.get_administrativo(codigo)

@ns.route('/<string:codigo>/extensao')
class Extensao(Resource):
    def get(self, codigo):
        return subunidade.get_extensoes(codigo)

@ns.route('/<string:codigo>/pesquisa')
class Pesquisa(Resource):
    def get(self, codigo):
        return subunidade.get_pesquisas(codigo)

@ns.route('/<string:codigo>/monitoria')
class Monitorias(Resource):
    def get(self, codigo):
        return subunidade.get_monitorias(codigo)

@ns.route('/<string:codigo>/documento')
class Documentos(Resource):
    def get(self, codigo):
        return subunidade.get_documentos(codigo)

'''
