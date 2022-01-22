import logging

from fastapi import FastAPI

from .server import router as server_router
from ..settings import settings


logger = logging.getLogger(__name__)


api = FastAPI(title=f'{settings.APP_NAME} API',
              description='',
              version=settings.VERSION,
              docs_url='/')


tags_metadata = [
    {
        'name': 'Server',
        'description': 'Server Endpoints'
    }
]

# Include Endpoint Routers
api.include_router(server_router, prefix='/server', tags=['Server'])


# Version Route
@api.get('/version')
def _get_version():
    return {'version': settings.VERSION}
