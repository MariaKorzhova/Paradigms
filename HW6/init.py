import time

# ДЗ: исправить ошибки подсчета времени, добавить комментарии, описать какую парадигму использовали.

#  Класс Stopwatch написан в стиле объектно-ориентированной парадигмы программирования. Данный класс содержит методы для запуска, паузы, возобновления, остановки и 
# получения времени работы секундомера.

# Исправлены ошибки в строках 42 и 48.

class Stopwatch:
    def __init__(self):  # конструктор класса
        self.start_time = None  # Время начала работы секундомера
        self.bool_pause_time = False  # Переменная, указывающая, находится ли секундомер в режиме паузы
        self.pause_start_time = None  # Время начала паузы
        self.total_paused_time = 0  # Общее время пауз

    def start(self):  # запускает секундомер или возобновляет его работу после паузы
        if not self.start_time:  # Если секундомер еще не запущен запускаем секундомер
            self.start_time = time.time()
        elif self.bool_pause_time:  # Если секундомер находится в режиме паузы учитываем время паузы
            self.total_paused_time += time.time() - self.pause_start_time 
            self.bool_pause_time = False  # Выходим из режима паузы

    def pause(self):  # приостанавливает работу секундомера
        if self.start_time and not self.bool_pause_time:  # Если секундомер запущен и не находится в режиме паузы
            self.bool_pause_time = True  # Входим в режим паузы
            self.pause_start_time = time.time()  # Запоминаем время начала паузы

    def resume(self):  # возобновляет работу секуномера после паузы
        if self.bool_pause_time:  # Если секундомер находится в режиме паузы
            self.bool_pause_time = False  # Выходим из режима паузы
            self.total_paused_time += time.time() - self.pause_start_time  # Учитываем время паузы

    def stop(self):  # останавливает секундомер и сбрасывает все переменные
        self.start_time = None  # Сбрасываем все переменные секундомера
        self.bool_pause_time = False
        self.pause_start_time = None
        self.total_paused_time = 0

    def get_time(self):  # возвращает время работы секундомера в секундах
        if self.start_time:
            if self.bool_pause_time:  
                return self.pause_start_time - self.start_time - self.total_paused_time
            else:
                return time.time() - self.start_time - self.total_paused_time

    def get_time_format(self):  # возвращает время работы секундомера в формате "минуты:секунды"
        time = int(self.get_time()) if self.get_time() is not None else 0
        min = time // 60
        sec = time % 60
        return f"{min:02}: {sec:02}"


if __name__ == "__main__": 
    name = Stopwatch()
    # выводятся доступные опции управления, и пользователь выбирает одну из них.
    while True:
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ")
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            name.stop()
        elif choice == "5":
            print("Exit")
            break
# После выхода из цикла выводится общее время работы секундомера
    total = name.get_time_format()
    print("time", total)