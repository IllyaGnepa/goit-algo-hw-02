from collections import deque

def is_palindrome(s: str) -> bool:
    # Приведення рядка до нижнього регістру та видалення пробілів
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Створення двосторонньої черги
    deq = deque(cleaned_str)
    
    # Порівняння символів з обох кінців
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True

# Приклад використання
input_str = input("Введіть рядок для перевірки: ")
if is_palindrome(input_str):
    print(f"'{input_str}' є паліндромом.")
else:
    print(f"'{input_str}' не є паліндромом.")