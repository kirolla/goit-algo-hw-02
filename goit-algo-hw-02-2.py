from collections import deque

def is_palindrome(input_string):
    # Видаляємо пробіли та переводимо рядок в нижній регістр
    input_string = input_string.replace(" ", "").lower()
    
    # Створюємо двосторонню чергу та додаємо символи рядка до неї
    char_queue = deque()
    for char in input_string:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги, поки черга не стане порожньою або зостанеться один символ
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True