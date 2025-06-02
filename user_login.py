import random
import string

class Captcha:
    def __init__(self):
        self.question = ""
        self.answer = ""

    def generate(self):
        # Simple math captcha: add two numbers
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        self.question = f"What is {a} + {b}?"
        self.answer = str(a + b)

    def verify(self, user_input):
        return user_input == self.answer

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserSystem:
    def __init__(self):
        self.users = {}  # store users as username: User object

    def register(self):
        print("=== User Registration ===")
        username = input("Enter username: ")
        if username in self.users:
            print("Username already exists!")
            return
        password = input("Enter password: ")

        captcha = Captcha()
        captcha.generate()
        print("CAPTCHA: ", captcha.question)
        user_answer = input("Enter CAPTCHA answer: ")

        if captcha.verify(user_answer):
            self.users[username] = User(username, password)
            print("Registration successful!")
        else:
            print("CAPTCHA verification failed. Registration aborted.")

    def login(self):
        print("=== User Login ===")
        username = input("Enter username: ")
        if username not in self.users:
            print("User not found.")
            return
        password = input("Enter password: ")
        user = self.users[username]
        if user.password != password:
            print("Incorrect password.")
            return

        captcha = Captcha()
        captcha.generate()
        print("CAPTCHA: ", captcha.question)
        user_answer = input("Enter CAPTCHA answer: ")

        if captcha.verify(user_answer):
            print(f"Login successful! Welcome, {username}.")
        else:
            print("CAPTCHA verification failed. Login aborted.")

def main():
    system = UserSystem()
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            system.register()
        elif choice == '2':
            system.login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
