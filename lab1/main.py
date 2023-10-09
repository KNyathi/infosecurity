import random
import string

def generate_password(identifier, length):
    q = len(identifier) % 5
    p = len(identifier) % 6

    lowercase_letters = ''.join(random.choices(string.ascii_lowercase, k=q))
    uppercase_letters = ''.join(random.choices(string.ascii_uppercase, k=p))
    digits = ''.join(random.choices(string.digits, k=1))
    special_characters = ''.join(random.choices(string.punctuation, k=1))

    # Generate the remaining characters
    remaining_characters = ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=length - q - p - 2))

    password = lowercase_letters + uppercase_letters + digits + special_characters + remaining_characters
    shuffled_password = ''.join(random.sample(password, len(password)))

    return shuffled_password

# Ввод идентификатора
identifier = input("Введите идентификатор пользователя: ")

# Задайте желаемую длину пароля
password_length = 12  # Заданное значение M


# Генерация пароля
password = generate_password(identifier, password_length)
# Вывод пароля
print("Сгенерированный пароль:", password)

