import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Функція для генерації нової заявки
def generate_request():
    request_id = random.randint(1000, 9999)  # Генерація унікального номера заявки
    print(f"Згенеровано заявку з ID: {request_id}")
    request_queue.put(request_id)

# Функція для обробки заявки
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробляється заявка з ID: {request_id}")
        time.sleep(1)  # Імітація часу на обробку заявки
        print(f"Заявка з ID: {request_id} оброблена")
    else:
        print("Черга пуста, немає заявок для обробки")

# Головний цикл програми
def main():
    while True:
        user_input = input("Введіть 'n' для створення нової заявки або 'p' для обробки заявки ('q' для виходу): ").strip().lower()
        if user_input == 'n':
            generate_request()
        elif user_input == 'p':
            process_request()
        elif user_input == 'q':
            print("Програма завершена.")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()