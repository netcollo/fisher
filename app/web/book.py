from flask import jsonify, request
from app.forms.book import SearchForm

from app.spider.yushu_book import YuShuBook
from app.libs.helper import is_isbn_or_key
from . import web

@web.route('/book/search')
def search():
    # # 至少药有一个字符，长度限制
    # q = request.args['q']
    # # 正整数，长度限制
    # page = request.args['page']

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)