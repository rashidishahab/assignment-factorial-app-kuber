import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"


def get_env(var):
    return os.environ[var]


file_path = join(dirname(__file__), '.env')

dotenv_path = join(file_path)
if os.path.isfile(file_path):
    load_dotenv(file_path)

APP_LANG = get_env("APP_LANG")
DEBUG = get_env("DEBUG")
HOST = get_env("HOST")
PORT = get_env("PORT")



X_API_KEY = get_env("X_API_KEY")

