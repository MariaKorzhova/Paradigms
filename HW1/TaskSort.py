# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    numbers = [3, 5, 4, 1, 2]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)
    return numbers



# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    numbers = [3, 5, 4, 1, 2]
    numbers.sort(reverse=True)
    print(numbers)



numbers = [3, 5, 4, 1, 2]
sort_list_imperative(numbers)
sort_list_declarative(numbers)
  