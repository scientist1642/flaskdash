"""Flask config."""
from os import environ, path

#from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Flask configuration variables."""

    # General Config
    # TODO read keys from environ
    FLASK_APP = "wsgi.py"
    FLASK_ENV = '123132' #environ.get("FLASK_ENV")
    SECRET_KEY = '123123' #environ.get("SECRET_KEY")

