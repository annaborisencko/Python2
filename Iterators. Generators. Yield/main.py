from time import sleep

from Parrot import Parrot, NewParrot, NewParrotLimit, parrot, simple_parrot
from Range import MyRange, my_range

list()

numbers = [1, 2, 3, 4]
# for num in numbers:
#     print(num)

# iterator = iter(numbers)    # numbers.__iter__()
# print(next(iterator))
# print(next(iterator))
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# for num in numbers:
#     print(num)

# iterator = iter(numbers)
# while True:
#     try:
#         item = next(iterator)
#         print(item)
#     except StopIteration:
#         break

# parrot = Parrot('Попка')
# for swear_word in parrot:
#     print(swear_word)


# parrot = NewParrot('Попка')
# for swear_word in parrot:
#     print(swear_word)


# parrot = NewParrotLimit('Попка', 3)
# for swear_word in parrot:
#     print(swear_word)

# for i in range(4):
#     print(i)
#
# for i in range(1, 4):
#     print(i)

# for i in range(3, 19, 4):
#     print(i)

# for i in MyRange(4):
#     print(i)
# print()
#
# for i in MyRange(1, 4):
#     print(i)
# print()
#
# for i in MyRange(3, 19, 4):
#     print(i)
# print()


# Итерируемый объект — это объект, который можно перебирать.
#
# За правило перебора отвечает итератор, а не сам объект.
#
# Итерируемый объект при попытке его перебрать должен уметь возвращать свой итератор, чтобы уже с ним продолжалась работа.
#
# Метод, который возвращает итератор, называется __iter__.
#
# Объект-итератор должен иметь метод __next__, который возвращает очередное значение.
#
# Цикл for будет вызывать функцию next от итератора до тех пор, пока не получит исключение StopIteration.
#
# Возникновение StopIteration — это ответственность итератора, а именно его метода __next__.
#
# Если StopIteration не возникнет никогда, то мы получим бесконечный цикл.

# lst_1 = []
# lst_2 = []
# for i in range(100_000):
#     lst_1.append(i)
# for i in range(100_000_000):
#     lst_2.append(i)
#
from sys import getsizeof
# print(getsizeof(lst_1))
# print(getsizeof(lst_2))
#
# iterator_1 = MyRange(100_000)
# iterator_2 = MyRange(100_000_000_000)
# print(getsizeof(iterator_1))
# print(getsizeof(iterator_2))


# def simple_generator():
#     yield 10
#     yield 2
#     yield 333
#     yield 5

# def simple_generator(limit):
#     i = 1
#     while i < limit:
#         yield i
#         i += 1

# generator = simple_generator(5)
# print(next(generator))
# print(next(generator))

# for item in simple_generator(5):
#     print(item)


# for word in parrot(7):
#     print(word)
#
#
# for i in my_range(3, 19, 4):
#     print(i)

# for word in simple_parrot():
#     print(word)


# def func():
#     return 1
#     yield 2
#
# for i in func():
#     print(i)

# iterator_1 = MyRange(100_000)
# iterator_2 = MyRange(100_000_000_000)
# print(getsizeof(iterator_1))
# print(getsizeof(iterator_2))
# generator_1 = my_range(0, 100_000)
# generator_2 = my_range(0, 100_000_000_000)
# print(getsizeof(generator_1))
# print(getsizeof(generator_2))


# list_1 = []
# for i in range(10):
#     if i % 2 == 0:
#         list_1.append(i ** 2)
#
# # list_2 = [i ** 2 for i in range(10) if i % 2 == 0]
# list_2 = [
#     i ** 2
#     for i in range(10)
#     if i % 2 == 0
# ]

# print(list_1)
# print(list_2)


# list_1 = [i ** 2 for i in range(100_000_000) if i % 2 == 0]
# generator_1 = (i ** 2 for i in range(100_000_000) if i % 2 == 0)
# print(getsizeof(list_1))
# print(getsizeof(generator_1))

generator_1 = (i for i in range(1000) if i % 10 == 0)
generator_2 = (i ** 2 for i in generator_1 if i % 3 == 0)
for i in generator_2:
    print(i)


set_1 = {i ** 2 for i in range(100) if i % 2 == 0}
dict_1 = {str(i): i ** 2 for i in range(100) if i % 2 == 0}
print(set_1)
print(dict_1)




# Итератор:
# * Когда нужен полный контроль над процессом итерации
# * когда у объекта естб другие методы и/или атрибуты
# * Подходит для сложных структур
# Генератор:
# * быстро создать итератор для обхода данных
# * подходит для простых случаев, таких как обход последовательности


