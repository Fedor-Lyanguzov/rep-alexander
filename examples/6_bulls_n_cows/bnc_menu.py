import logging
from bulls_n_cows import game, StopGame
logging.basicConfig(level=logging.DEBUG)

def exit():
    print("До свидания!")
    raise SystemExit

while True:
    try:
        command = input("Play, scores or exit?")
        if command == "play":
            game()
        elif command == "scores":
            pass
        elif command == "exit":
            exit()
        else:
            raise ValueError
    except ValueError:
        print("Неверная команда")
    except StopGame:
        pass
