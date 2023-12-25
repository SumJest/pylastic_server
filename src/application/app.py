import secrets
from pathlib import Path

from flask import Flask

BASE_DIR = Path(__file__).resolve().parent.parent


app = Flask(__name__, template_folder=BASE_DIR / 'templates')
app.secret_key = secrets.token_hex(20)
from application import views