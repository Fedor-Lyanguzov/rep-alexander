pos = [ x for x in ">>> <<<" ]
final_pos = [ x for x in "<<< >>>"]

def swap(pos, i1, i2):
    pos[i1], pos[i2] = pos[i2], pos[i1]
    
class IllegalCommand(Exception):
    pass

guessed = False
while not guessed:
    print(''.join(str(x) for x in range(7)))
    print(''.join(pos))
    try:
        cmd = int(input("Введите номер стрелки(0-6): "))
        if pos[cmd] == ">":
            if pos[cmd+1] == " ":
                swap(pos, cmd, cmd+1)
            elif pos[cmd+2] == " ": 
                swap(pos, cmd, cmd+2)
            else:
                raise IllegalCommand
        elif pos[cmd] == "<":
            if pos[cmd-1] == " ":
                swap(pos, cmd, cmd-1)
            elif pos[cmd-2] == " ": 
                swap(pos, cmd, cmd-2)
            else:
                raise IllegalCommand
        else:
            raise IllegalCommand
    except IllegalCommand:
        print("Неверная команда")
    else:
        if pos == final_pos:
            print(pos)
            guessed = True

print("Победа!")
