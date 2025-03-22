import threading
import time

# Создаем блокировку для синхронизации вывода
print_lock = threading.Lock()


class CountdownThread(threading.Thread):
    def __init__(self, thread_name):
        super().__init__()
        self.thread_name = thread_name
        self.daemon = True  # Делаем поток демоном

    def run(self):
        with print_lock:
            print(f"{self.thread_name} начал выполнение.")

        for i in range(10, 0, -1):
            with print_lock:
                print(f"{self.thread_name}: {i}")
            time.sleep(1)  # Пауза 1 секунда

        with print_lock:
            print(f"{self.thread_name} завершил выполнение.")


# Создаем два демон-потока
thread1 = CountdownThread("Поток 1")
thread2 = CountdownThread("Поток 2")

# Запускаем потоки
thread1.start()
thread2.start()

# Даем демонам время на выполнение
time.sleep(12)  # Ждем, пока потоки завершат отсчет
print("Оба потока завершили свою работу.")