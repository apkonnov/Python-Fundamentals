from random import randrange


def get_jokes(num, flag):
    """ функция get_jokes() возвращает num шуток, flag разрешает или запрещает повторы слов в шутках """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if flag:  # повторы разрешены
        for i in range(num):
            jokes.append(nouns[randrange(len(nouns))] + ' ' + adverbs[randrange(len(adverbs))] + ' '
                         + adjectives[randrange(len(adjectives))])
    else:  # повторы запрещены
        num = min(num, len(nouns), len(adverbs), len(adjectives))
        for i in range(num):
            jokes.append(nouns.pop(randrange(len(nouns))) + ' ' + adverbs.pop(randrange(len(adverbs)))
                         + ' ' + adjectives.pop(randrange(len(adjectives))))
    return jokes


print(get_jokes(10, False))
