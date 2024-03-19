import string
import random


def generate_random_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    length = random.randint(10, 20)
    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)
