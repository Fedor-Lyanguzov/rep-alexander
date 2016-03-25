def countBulls(puzzle_num, user_num):
    bulls = 0
    for i in range(len(puzzle_num)):
        if puzzle_num[i] == user_num[i]:
            bulls += 1
    return bulls

def countCows(puzzle_num, user_num, bulls):
    cows = 0
    for i in range(len(puzzle_num)):
        for j in range(len(puzzle_num)):
            if puzzle_num[i] == user_num[j]:
                cows += 1
                # При дубликатах в user_num сколько должно быть коров?
    return cows - bulls        

def countScore(guess_count):
    """
    При кол-ве попыток >100 спросить, хочет ли играть дальше
    см. функцию очков от попыток в тетради
    """
    if guess_count<5:
        return 500000
    elif guess_count<100:
        return (-99/95*guess_count + 95)*1000000
    else:
        return 10000
