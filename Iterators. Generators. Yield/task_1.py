# 1. Доработать класс `FlatIterator` в коде ниже. Должен получиться итератор, 
# который принимает список списков и возвращает их плоское представление, 
# т. е. последовательность, состоящую из вложенных элементов. 
# Функция `test` в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_cursor = 0
        self.item_cursor = 0
        return self

    def __next__(self):
        if self.item_cursor == len(self.list_of_list[self.list_cursor]):
            self.item_cursor = 0
            self.list_cursor += 1
        if self.list_cursor == len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.list_cursor][self.item_cursor]
        self.item_cursor += 1
        return item

# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
# # flat = FlatIterator(list_of_lists_1)
# # for item in flat:
# #     print(item)
# list_zip = zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     )
# for flat_iterator_item, check_item in list_zip:
#     print(flat_iterator_item, check_item)
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
