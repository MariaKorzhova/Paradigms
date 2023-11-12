# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

from functools import reduce

first_list = [33, 46, 12, 1]

second_list = [8, 101, 35, 4]


if __name__ == '__main__':
    print(*map(lambda x, y: x / y, [(sum((xb - reduce(lambda x, y: x + y, first_list) / 
        reduce(lambda x, y: x + 1, first_list)) * (ya - reduce(lambda x, y: x + y, second_list) / 
        reduce(lambda x, y: x + 1, second_list)) for xb, ya in zip(first_list, second_list)))], 
        [(sum((xb - reduce(lambda x, y: x + y, first_list) / reduce(lambda x, y: x + 1, first_list))
        ** 2 for xb in first_list) ** 0.5 * (sum((ya - reduce(lambda x, y: x + y, second_list) /
        reduce(lambda x, y: x + 1, first_list)) ** 2 for ya in second_list) ** 0.5))]))