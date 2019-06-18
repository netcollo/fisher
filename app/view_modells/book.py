class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books' : [],
            'total' : 0,
            'keyword' : keyword
        }
        if data:
            returned['total'] = 1
            returned['book'] = [cls.__cut_book_data(data)]
        pass
    
    @classmethod
    def package_collection(cls, keyword):
        pass

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title' : data['title'],
            'publisher' : data['publisher'],
            'pages' : data['pages'],
            'author' : '、'.join(data['author']),
            'price' : data['price'],
            'summary' : data['summary'],
            'image' : data['image']
        }