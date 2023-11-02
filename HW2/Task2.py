# Переписать алгоритм в процедурном стиле
# Структурное программирование

# Определение функции merge_sort, которая выполняет сортировку методом слияния.

# def merge_sort(arr):
#     if len(arr) > 1: # Проверка, что длина массива больше 1 (иначе сортировка не нужна).
#         mid = len(arr) // 2 # Вычисление середины массива.
#         left_half = arr[:mid] # Создание левой половины массива.
#         right_half = arr[mid:] # Создание правой половины массива.

#     # Рекурсивный вызов merge_sort для левой и правой половин массива.
#     merge_sort(left_half)
#     merge_sort(right_half)

#     i = j = k = 0  # Инициализация индексов для объединения двух половин.

#     # Объединение левой и правой половин в один отсортированный массив.
#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
#             arr[k] = left_half[i]  # Если элемент из левой меньше, помещаем его в исходный массив.
#             i += 1
#         else:
#             arr[k] = right_half[j]  # Если элемент из правой меньше, помещаем его в исходный массив.
#             j += 1
#         k += 1

#     # Добавление оставшихся элементов из левой и правой половин (если такие есть).
#     while i < len(left_half):
#         arr[k] = left_half[i]
#         i += 1
#         k += 1

#     while j < len(right_half):
#         arr[k] = right_half[j]
#         j += 1
#         k += 1


def merge(left_half, right_half): # Создаём процедуру слияния, которая объединяет два упорядоченных массива в один
    l_left_half, l_right_half = len(left_half), len(right_half)
    arr = [None for i in range(l_left_half + l_right_half)] # Создаём список для слияния
    i = j = k = 0
    while i < len(left_half) and j < len(right_half): # Объединение левой и правой половин в один отсортированный массив.
        if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
            arr[k] = left_half[i]  # Если элемент из левой меньше, помещаем его в исходный массив.
            i += 1
        else:
            arr[k] = right_half[j]  # Если элемент из правой меньше, помещаем его в исходный массив.
            j += 1
        k += 1


    while i < len(left_half): # Добавление оставшихся элементов из левой и правой половин (если такие есть).
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr): # Создаём процедуру сортировки слиянием
    l_arr = len(arr)
    if l_arr == 1 or l_arr == 0: # обрабатываем исключение, если массив нулевой или имеет один элемент
        return arr
    left_half, right_half = arr[0 : l_arr // 2], arr[l_arr // 2 : l_arr] # разделение массива на две половины
    left_half, right_half = merge_sort(left_half), merge_sort(right_half) # вызываем рекурсию сортировки для левой и правой частей массива
    mg = merge(left_half, right_half) # объединяем упорядоченные половины
    for i in range(l_arr):
        arr[i] = mg[i]
    return arr

my_array = [64, 34, 25, 12, 22, 11, 90] # Создание неотсортированного массива.
merge_sort(my_array) # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", my_array) # Вывод отсортированного массива.