from flask import Flask
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import jsonify

app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)