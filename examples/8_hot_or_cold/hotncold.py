import random
import math

def comparison(number,a,b):        
    module1 = math.fabs(number - b)
    module2 = math.fabs(number - a)
    if (module1 < module2):
        return 1
    elif (module1 > module2):
        return 2
    else:
        if (a == b):
            return 3
        else :
            return 4

def get_first_number():
    good_number = False
    while not good_number:
        try:
            ghf = int(input("Введите целое число: "))
        except ValueError:
            print ("Неверное число")
        else:
            good_number = True
            return ghf

if __name__ == "__main__":
    guessed = False

    number = random.randrange(100)
            
    a = get_first_number()

    while not guessed:
        try:
            b = int(input("Введите следующее целое число: "))
        except ValueError:
            print ("Неверное число")
        else:
            c = comparison(number,a,b)
            if c == 1:
                print("Теплее")
            elif c == 2:
                print("Холоднее")
            elif c == 3:
                print ("Введите другое число")
            elif c == 4:
                print ("Не теплее и не холоднее")
            if ( a == number or b == number):
                guessed = True
            a = b
        
    print("Я загадал",number)
