from random import randint

def compare(pc, user):
    if user == 1 and pc == 1:
        return "draw" 
    elif user == 1 and pc == 2:
        return "you lose"
    elif user == 1 and pc == 3:
        return "you win"
    elif user == 2 and pc == 1:
        return "you win"
    elif user == 2 and pc == 2:
        return "draw" 
    elif user == 2 and pc == 3:
        return "you lose"
    elif user == 3 and pc == 1:
        return "you lose"
    elif user == 3 and pc == 2:
        return "you win"
    elif user == 3 and pc == 3: 
        return "draw"

while True:
    pc_choice = randint(1,3)

    try:
        user_input = int(input("""
            choose your choice lol:
            1. rock
            2. paper
            3. scissors
            4. end game
        """))

        if user_input not in range(1,4):
            if user_input < 5:
                break
            else:
                print("invalid choice")
        else: 
            print("you" + str(user_input))
            print("pc:" + str(pc_choice))

            print(compare(user_input, pc_choice))

    except: 
        print("invalid choice")