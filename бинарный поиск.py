import math 

class IllegalCommand(Exception):
   pass

class exit(Exception):
    pass
h = False
while not h :
    guessed = False
    while not guessed:
        print ("��������� ����� ����� �� 1 �� 99")
	    print ("1 - ����������, 2 - �����, 3 - ������� ����")
	    cmd = int [input()]
	    lstvaluesH = False 
	    lstvaluesL = False
    	razn = 25 
    	if cmd == 2:
	    raise exit
        elif cmd == 1:
    	    Expected_value == 50
    	    useranswer =  input("���������� ����� -" Expected_value )
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
    		    print ("������� �� ����")
    	elif cmd == 3:
    	    print ("��������� ����� �� 1 �� 99. ��������� ����� �������� ��� ��������, ������ �������� �� �����. ���� ���������� �������� ������ - ������� (+), ������ - (-), ���� ����� �������� - (=) . ��� ������ ������� (0)")
    	else:
    	    raise IllegalCommand
	
