import random
import logging
from bnc_utils import countBulls, countCows, countScore

class StopGame(Exception):
    pass


# Загадать четырехзначное число с неповторяющимися цифрами
def game():
    nums = [x for x in range(10)]
    puzzle_num = random.sample(nums, 4)
    logging.debug(puzzle_num)

    # Пока число не отгадано:
    guessed = False
    guess_count = 0
    while not guessed:

        guess_count += 1
        # Спросить у пользователя число
        try:
            command = input('Введите число или exit: ')
            if command == "exit":
                raise StopGame
            user_num = [ int(character) for character in command ]
            # Проверить, что их 4 ?
            if len(user_num) != 4:
                raise ValueError
        # Проверить, что это цифры ?
        except ValueError:
            print('Введите 4 цифры!')
        else:

            # Посчитать быков
            bulls = countBulls(puzzle_num, user_num)

            # Посчитать коров
            cows = countCows(puzzle_num, user_num, bulls)

            # Если пользователь угадал:
            if bulls == 4:
                guessed = True
                # Пишем "победа!"
                print("Победа!")
                print("Ваши очки:", countScore(guess_count))
            # Иначе:
            else:
                # Вывести быков и коров
                print("Быков:", bulls, "Коров:", cows)
     

