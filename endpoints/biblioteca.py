from flask_restplus import Resource, reqparse
from restplus import api as liveapi
from ufma_scrapper import acervobiblioteca
from flask import request

ns = liveapi.namespace('biblioteca', description='Operations related to "biblioteca"')

get_arguments = reqparse.RequestParser()
get_arguments.add_argument('titulo', type=str, required=False, help='Título do livro')
get_arguments.add_argument('autor', type=str, required=False, help='Autor do livro')


@ns.route('/acervo/<string:idtitulo>')
class Acervo(Resource):
    def get(self, idtitulo):
        livro = acervobiblioteca.extrai_marc_to_json(idtitulo)
        if (livro):
            return livro
        else:
            return {'message': "recurso não encontrado"}, 404

@ns.route('/acervo/')
class AcervoCollection (Resource):
    @liveapi.expect(get_arguments, validate=True)
    def get(self):
        titulo = request.args.get("titulo")
        autor = request.args.get("autor")
        limit = request.args.get("limit")
        acervo = acervobiblioteca.get_acervo(titulo, autor, limit)
        return acervo


