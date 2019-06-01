#判断输入的内容是否为isbn
def is_isbn_or_key(word):
    """
    
    """
    isbn_or_key = 'key'
    # ISDN ： 一种为13位0至9的数字
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isdn'

    # ISDN ： 10位0至9的数字，其中包含不定数量的'-'， 
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isdn'
    return isbn_or_key