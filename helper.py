#判断输入的内容是否为ISDN
def is_isdn_or_key(word):
    isdn_or_key = 'key'
    # ISDN ： 一种为13位0至9的数字
    if len(word) == 13 and word.isdigit():
        isdn_or_key = 'isdn'

    # ISDN ： 10位0至9的数字，其中包含不定数量的'-'， 
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isdn_or_key = 'isdn'
    return isdn_or_key