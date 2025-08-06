# 3.__*__ Необязательное задание. 
# Написать итератор, аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.current_list = self.get_current_list(self.list_of_list)
        return self
    
    def __next__(self):
        # print(self.current_list)
        if self.cursor == len(self.current_list):
            raise StopIteration
        item = self.current_list[self.cursor]
        self.cursor += 1
        # print(self.cursor)
        return item
    
    def get_current_list(self, list_of_list):
        result = []
        for list_item in list_of_list:
            if type(list_item) == list:
                result.extend(self.get_current_list(list_item))
            else:
                result.append(list_item) 
        return result

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()