from flask import Flask
from helper import is_isdn_or_key

app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def search(q, page):
    isdn_or_key = is_isdn_or_key(q)