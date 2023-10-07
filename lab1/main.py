import random
import string

def generate_password(identifier, length):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters")

    q = len(identifier) % 5
    p = len(identifier) % 6

    # Ensure at least one uppercase letter, special character, and number
    if length - q - p < 3:
        raise ValueError("Password length is too short to meet requirements")

    lowercase_letters = ''.join(random.choices(string.ascii_lowercase, k=q))
    uppercase_letters = ''.join(random.choices(string.ascii_uppercase, k=1))
    digits = ''.join(random.choices(string.digits, k=1))
    special_characters = ''.join(random.choices(string.punctuation, k=1))

    # Generate the remaining characters
    remaining_characters = ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=length - q - p - 3))

    password = lowercase_letters + uppercase_letters + digits + special_characters + remaining_characters
    shuffled_password = ''.join(random.sample(password, len(password)))

    return shuffled_password

# Ввод идентификатора
identifier = input("Введите идентификатор пользователя: ")

# Задайте желаемую длину пароля
password_length = 12  # Заданное значение M

try:
    # Генерация пароля
    password = generate_password(identifier, password_length)
    # Вывод пароля
    print("Сгенерированный пароль:", password)
except ValueError as e:
    print("Ошибка:", str(e))
