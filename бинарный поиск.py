import math 

class IllegalCommand(Exception):
   pass

class exit(Exception):
    pass
h = False
while not h :
    guessed = False
    while not guessed:
        print ("Загадайте целое число от 1 до 99")
	    print ("1 - продолжить, 2 - выход, 3 - правила игры")
	    cmd = int [input()]
	    lstvaluesH = False 
	    lstvaluesL = False
    	razn = 25 
    	if cmd == 2:
	    raise exit
        elif cmd == 1:
    	    Expected_value == 50
    	    useranswer =  input("Загаданное число -" Expected_value )
        	if useranswer == 0:
    		    raise exit
    		elif useranswer == "+"
    		    Expected_value = Expected_value + razn
    			lstvaluesH = True
    			print Expected_value
    			razn = razn / 5 
    	    elif useranswer == "-":
    		    Expected_value = Expected_value - razn
    			lstvaluesL = True
    			print Expected_value
    		elif useranswer == "=":
    		    print ("Спасибо за игру")
    	elif cmd == 3:
    	    print ("Загадайте число от 1 до 99. Программа будет пытаться его отгадать, выводя значения на экран. Если загаданное значение больше - введите (+), меньше - (-), если число угаданно - (=) . Для выхода введите (0)")
    	else:
    	    raise IllegalCommand
	
