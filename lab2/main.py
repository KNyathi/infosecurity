import re
import string
import datetime

class User:
    def __init__(self, username, password, full_name, date_of_birth, city_of_birth, phone_number):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.city_of_birth = city_of_birth
        self.phone_number = phone_number


    def check_password(self, password):
        return self.password == password


    def change_password(self, new_password, date_of_birth):
        if new_password == date_of_birth.strftime('%d.%m.%Y') or new_password == date_of_birth.strftime('%d/%m/%Y'):
            return False, "New password cannot match the date of birth."

        if len(new_password) != 10:
            return False, "New password length should be 10 characters."

        allowed_characters = string.digits + string.punctuation
        if not all(char in allowed_characters for char in new_password):
            return False, "New password should only contain digits and punctuation."

        self.password = new_password
        return True, "Password changed successfully."


user_data = {
    "user1": User("user1", "password1", "John Doe", datetime.date(1990, 5, 15), "Moscow", "1234567890"),
    "user2": User("user2", "password2", "Jane Smith", datetime.date(1985, 8, 20), "St Petersburg", "9876543210")
}


def authenticate_user(username, password):
    user = user_data.get(username)
    if user and user.check_password(password):
        return True, user
    else:
        return False, None


def change_password(username, new_password, date_of_birth):
    user = user_data.get(username)
    if user:
        success, message = user.change_password(new_password, date_of_birth)
        return success, message
    else:
        return False, "User not found."


def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        pass

    try:
        datetime.datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def display_resource():
    with open("resource.txt", "r") as file:
        content = file.read()
        print("Resource content:\n" + content)


def main():
    global user
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        authenticated, user = authenticate_user(username, password)

        if authenticated:
            print("Authentication successful! Welcome, " + user.full_name)
            print("Resource access:")
            display_resource()
            break  # Exit the loop since authentication was successful
        else:
            print("Authentication failed. Invalid username or password.")
            

if __name__ == "__main__":
    print("Authentication Test")
    main()  # Call the main function to start authentication and resource access
    print("\nPassword Change Test")
    
    username = input("Enter your username: ")
    current_password = input("Enter your current password: ")
    new_password = input("Enter your new password: ")

    if is_valid_date(user.date_of_birth.strftime('%d.%m.%Y')):
        date_of_birth = datetime.datetime.strptime(user.date_of_birth.strftime('%d.%m.%Y'), '%d.%m.%Y').date()
    else:
        date_of_birth = datetime.datetime.strptime(user.date_of_birth.strftime('%d/%m/%Y'), '%d/%m/%Y').date()

    success, message = change_password(username, new_password, date_of_birth)
    if success:
        print(message)
    else:
        print("Password change failed:", message)
        
        
        
        
