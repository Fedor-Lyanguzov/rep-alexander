##import math 
##
##class IllegalCommand(Exception):
##   pass
##
##class exit(Exception):
##    pass
##   
##h = False
##while not h :
##    guessed = False
##    while not guessed:
##        print ("Загадайте целое число от 1 до 99")
##        print ("1 - продолжить, 2 - выход, 3 - правила игры")
##        cmd = int (input())
##        lstvaluesH = False 
##        lstvaluesL = False
##        razn = 25
##        if cmd == 2:
##           raise exit
##        elif cmd == 1:
##            Expected_value = 50
##            useranswer =  input("Загаданное число - " +str(Expected_value) )
##            if useranswer == 0:
##                raise exit
##            elif useranswer == "+":
##                Expected_value = Expected_value + razn
##                lstvaluesH = True
##                print (Expected_value)
##                razn = razn / 5 
##            elif useranswer == "-":
##                Expected_value = Expected_value - razn
##                lstvaluesL = True
##                print (Expected_value)
##            elif useranswer == "=":
##                print ("Спасибо за игру")
##        elif cmd == 3:
##            print ("Загадайте число от 1 до 99. Программа будет пытаться его отгадать, выводя значения на экран. Если загаданное значение больше - введите (+), меньше - (-), если число угаданно - (=) . Для выхода введите (0)")
##        else:
##            raise IllegalCommand

class Cheating(Exception):
   pass
class ToMenu(Exception):
   pass

playing = True
while playing:
   print ("Что вы хотите делать?\n 1 - новая игра\n 2 - правила игры\n 3 - выход\n")
   cmd = input()
   if cmd == "1":
      try:
         numbers = [ x for x in range(1,100) ]
         guessed = False
         while not guessed:
            print(numbers)
            if not numbers:
               raise Cheating
            expected_value = numbers[len(numbers)//2]
            user_input = input("Вы загадали {}?".format(expected_value))
            if user_input == "-":
               numbers = numbers[ : len(numbers)//2]
            if user_input == "+":
               numbers = numbers[len(numbers)//2 +1: ]
            if user_input == "=":
               guessed = True
               print("Ура, я угадал!")
            if user_input == "0":
               raise ToMenu
      except Cheating:
         print("Нечестно! Я не буду с вами играть!")
         playing = False
      except ToMenu:
         pass
            
   elif cmd == "2":
       print ("""
Загадайте число от 1 до 99.
Программа будет пытаться его отгадать, выводя значения на экран.
Если загаданное значение больше - введите (+), меньше - (-), если число угаданно - (=) .
Для выхода введите (0)""")
   elif cmd == "3":
      playing = False
   else:
      print("Неверная команда")


   




    
