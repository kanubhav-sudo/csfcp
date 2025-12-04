import random
print('welcome to number guessing game')
secret_number = random.randint(1, 100)
attempts = 0
while True:
    user_input = input('enter your guess between 1 to 100 or type "exit" to quit: ')
    if user_input.lower() == 'exit':
        print(f'you exited the game. the secret number was {secret_number}.')
        break
    try:
        guess = int(user_input)
        attempts += 1
        if guess < 1 or guess > 100:
            print('please guess a number within the range of 1 to 100.')
            continue
        if guess < secret_number:
            print('too low! try again.')
        elif guess > secret_number:
            print('too high! try again.')
        else:
            print(f'congratulations! you guessed the number {secret_number} in {attempts} attempts.')
            break
    except ValueError:
        print('invalid input. please enter a valid number or "exit" to quit.')
