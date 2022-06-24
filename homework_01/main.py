"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return([number**2 for number in numbers])

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    if number == 0 or number == 1:
        return False
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return (list(filter(lambda x: x % 2 == 1, numbers)))

    if filter_type == EVEN:
        return (list(filter(lambda x: x % 2 == 0, numbers)))

    if filter_type == PRIME:
        return (list(filter(is_prime, numbers)))
