import random

def check_guess(secret, guess):
    if guess == secret:
        return "Победа!", True
    elif guess < secret:
        return "Больше", False
    else:
        return "Меньше", False

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Угадай число (1–100): "))
    message, is_win = check_guess(secret_number, guess)
    print(message)
    if is_win:
        break