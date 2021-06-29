from random import randint

playing = True

attempts = 0

random_num = randint(1, 100)

while playing:
    try:
        user_input = int(input("guess the number "))
        attempts += 1

        if user_input < random_num:
            print("go higher")
        elif user_input == random_num:
            print("you got it in " + str(attempts) + " attempts")

            playing = False

            while not playing:
                got_it_input = input("> play again, > end game ")
                
                if got_it_input == "play again":
                    playing = True
                    attempts = 0

                    random_num = randint(1, 100)
                elif got_it_input == "end game":
                    break
                else:
                    print("invalid input")
                    
                    continue
        else:
            print("go lower")
    except:
        print("invalid input")