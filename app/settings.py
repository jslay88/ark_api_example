import os
from pathlib import Path
from typing import Optional, Union

from pydantic import BaseSettings


def secret_from_file(path: Union[str, Path]) -> Optional[str]:
    """Check if file exists, if so, read single line"""
    if not isinstance(path, Path):
        path = Path(path)
    if not path.is_file():
        return
    with open(path, 'r') as f:
        return f.readline().strip()


class Settings(BaseSettings):
    APP_NAME: str = os.getenv('APP_NAME', 'api_example')
    MOD_IDENTIFIER: str = os.getenv('MOD_IDENTIFIER', 'api_example')
    SECRETS_DIR: str = os.getenv('SECRETS_DIR', f'/var/run/secrets/{APP_NAME}')
    DB_USER: str = secret_from_file(Path(SECRETS_DIR) / 'postgres/postgresql-username') or \
        os.getenv('DB_USER', 'postgres')
    DB_PASS: str = secret_from_file(Path(SECRETS_DIR) / 'postgres/postgresql-password') or \
        os.getenv('DB_PASS', 'postgres')
    DB_HOST: str = secret_from_file(Path(SECRETS_DIR) / 'postgres/postgresql-host') or \
        os.getenv('DB_HOST', 'postgres')
    DB_PORT: int = secret_from_file(Path(SECRETS_DIR) / 'postgres/postgresql-port') or \
        int(os.getenv('DB_PORT', 5432))
    DB_NAME: str = secret_from_file(Path(SECRETS_DIR) / 'postgres/postgresql-database') or \
        os.getenv('DB_NAME', 'postgres')
    SQLALCHEMY_DATABASE_URI: str = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    if LOG_LEVEL not in ['DEBUG', 'INFO', 'WARNING', 'CRITICAL']:
        LOG_LEVEL = 'INFO'

    VERSION = '1.0.0'


settings = Settings()
