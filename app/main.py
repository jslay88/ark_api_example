import os.path
import logging

from fastapi import FastAPI

from .api_v1 import api as api_v1
from .settings import settings


logger = logging.getLogger(__name__)

logger.setLevel(settings.LOG_LEVEL.upper())


def app():
    logger.info(f'Creating FastAPI Application for {settings.APP_NAME}...')
    _app = FastAPI()

    logger.info('Mounting APIs...')
    _app.mount('/api/v1', api_v1)

    logger.info('Mounting Health Check Endpoint...')
    @_app.get('/health')
    def health(): return {'health': 'healthy'}

    if os.path.isdir('static') and os.listdir('static'):
        from fastapi.staticfiles import StaticFiles
        logger.info('Mounting Static...')
        _app.mount('', StaticFiles(directory='static', html=True), name='static')

    logger.info('Application Created Successfully.')
    return _app
