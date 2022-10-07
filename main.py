import string
import random
pencil = input("How many pencils would you like to use:\n")

for j in pencil:
    if j not in string.digits:
        chk = True
        break
    else:
        chk = False
        
while chk:
    pencil = input("The number of pencils should be numeric\n")
    for i in pencil:
        if i in string.digits:
            chk = False
        else:
            chk = True
            break

while int(pencil) <= 0:
    pencil = input("The number of pencils should be positive\n")
    for i in pencil:
        for j in pencil:
            if j not in string.digits:
                chk = True
                break
            else:
                chk = False
        while chk:
            pencil = input("The number of pencils should be numeric\n")
            for i in pencil:
                if i in string.digits:
                    chk = False
                else:
                    chk = True
                    break
    
pencils = int(pencil)

players = ["John","bot"]

first_player = input("Who will be the first (John, bot):\n")

while first_player not in players:
    first_player = input("Choose between John and bot\n")
    
print("|"*pencils)

possible_values = ["1","2","3"]

pencils_taken = 0
while pencils > 0:
    bad_positions = list(range(1, pencils+1,4))
    if first_player == "John":
        pencils_taken = input("{first}'s turn:\n".format(first = first_player))
    if first_player == "bot":
        if pencils not in bad_positions:
            print("{player}'s turn:".format(player = first_player))
            if pencils > 1:
                pencils_taken = str(pencils - bad_positions[-1])
            else:
                pencils_taken = str(1)
            print(pencils_taken)
        else:
            print("{player}'s turn:".format(player = first_player))
            pencils_taken = str(1)
            print(pencils_taken)
    bad_positions = []
    while pencils_taken not in possible_values:
        pencils_taken = input("Possible values: '1', '2' or '3'\n")
    while int(pencils_taken) > int(pencils):
        pencils_taken = input("Too many pencils were taken\n")
    pencils = pencils - int(pencils_taken)
    print("|"*pencils)
    if first_player == "bot":
        first_player = "John"
    else:
        first_player = "bot"
    if pencils == 0 :
        print("{winner} won!".format(winner = first_player))
