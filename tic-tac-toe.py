board = """
 {0} | {1} | {2} 
___|___|___
 {3} | {4} | {5} 
___|___|___
 {6} | {7} | {8} 
   |   |   
"""

placements = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

turn = "o"
game_over = False

print("""
welcome to dehy's sensational masterpiece; tic-tac-toe, a totally original game idea!

input 'new' for new game or 'end' to gtfo.

""")
print(board.format(*placements))

while True:    
    try:    
        comm = input()
        
        if comm == "end": break
        elif comm == "new":
            placements = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            
            print(board.format(*placements))

            game_over = False
        else:
            if game_over:
                print("game over. input 'new' or 'end'.")
                continue
            
            i = int(comm)
            
            if placements[i] != " ":
                print("position taken.")
            
                continue
        
            if turn == "o":
                turn = "x"
            else:
                turn = "o"
            
            placements[i] = turn
            print(board.format(*placements))
            
            if placements[0] == placements[1] == placements[2] != " " or placements[3] == placements[4] == placements[5] != " " or placements[6] == placements[7] == placements[8] != " ":
                print(turn + " wins. finishing move: horizon flash!")
                
                game_over = True
            elif placements[0] == placements[3] == placements[6] != " " or placements[1] == placements[4] == placements[7] != " " or placements[2] == placements[5] == placements[8] != " ":
                print(turn + " wins. finishing move: vertical verdict of death!")
                
                game_over = True
            elif placements[0] == placements[4] == placements[8] != " " or placements[2] == placements[4] == placements[6] != " ":
                print(turn + " wins. finishing move: dia-gone-al slash!")
                
                game_over = True
            elif not " " in placements:
                print("no one wins. you guys are noob.")
                
                game_over = True
    except:
        print("invalid input.")
        
        continue