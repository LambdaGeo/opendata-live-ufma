import logging
from flask_restplus import Api
import settings


log = logging.getLogger(__name__)

api = Api(version='0.1', title='Live Rest UFMA API',
          description='Essa API extrai informações em tempo real de páginas públicas da UFMA')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500



