class Parrot:
    def __init__(self, name):
        self.name = name

    def fly(self):
        pass

    def eat(self):
        pass

    def __iter__(self):
        return VocabularyIterator()

class VocabularyIterator:
    def __init__(self):
        self.words = ['Карамба', 'На абордаж!', 'Тысяча чертей!', 'Пиастры']
        self.cursor = -1

    def __next__(self):
        self.cursor += 1
        if len(self.words) == self.cursor:
            raise StopIteration
        return self.words[self.cursor]


class NewParrot:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        self.cursor = -1
        self.words = ['Карамба', 'На абордаж!', 'Тысяча чертей!', 'Пиастры']
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.words) == self.cursor:
            raise StopIteration
        return self.words[self.cursor]

class NewParrotLimit:
    def __init__(self, name, limit):
        self.limit = limit
        self.name = name

    def __iter__(self):
        self.total = -1
        self.cursor = -1
        self.words = ['Карамба', 'На абордаж!', 'Тысяча чертей!', 'Пиастры']
        return self

    def __next__(self):
        self.total += 1
        self.cursor += 1
        if self.limit == self.total:
            raise StopIteration
        if self.cursor == len(self.words):
            self.cursor = 0
        return self.words[self.cursor]


def simple_parrot():
    yield from ['Карамба', 'На абордаж!', 'Тысяча чертей!', 'Пиастры']


def parrot(limit):
    words = ['Карамба', 'На абордаж!', 'Тысяча чертей!', 'Пиастры']
    cursor = -1
    for _ in range(limit):
        cursor += 1
        if cursor == len(words):
            cursor = 0
        yield words[cursor]