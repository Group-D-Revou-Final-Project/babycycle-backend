from .base import *  # noqa
import os
SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI_PROD")
SQLALCHEMY_TRACK_MODIFICATIONS = False