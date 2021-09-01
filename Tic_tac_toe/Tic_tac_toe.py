# Tic-Tac-Toe python
import math

class Game:

    def __init__(self, board, player_one_value, player_one, player_two_value, player_two):
        self.board = board
        self.player_one_value = player_one_value
        self.player_one = player_one
        self.player_two_value = player_two_value
        self.player_two = player_two
        

    def start_game(self):
        
        for i in self.board:
           print([i])
                      
        move = False
        tie = 0
        
        #while the players are playing continue the game
        while(playing):

            if move == False:
                print("\n", self.player_one, self.player_one_value, "is up")

                Game.place(self.board, self.player_one_value)
                move = True
                tie += 1
                if Game.check_win(self.board, self.player_one_value, self.player_one) == True:
                    break
                      
                #all options exhausted if not win output is tie
                if tie == 5:
                    print("Tie game! Try again!")
                    
                    break
                      
            
            if move == True:
                print("\n", self.player_two, self.player_two_value, "is up")
                Game.place(self.board, self.player_two_value)
                move = False
                if Game.check_win(self.board, self.player_two_value, self.player_two) == True:
                    break
                    
     
            
    #get the position of the board and replace that with the value
    def place(board, value):
        print("\n")

        while True:
            try:
                print("type the number 1-9 where you want to place")
                number = int(input())
                if(number in input_list):               
                    input_list.remove(number)
                    break
                else:
                    print("space is invalid taken please try again")
            except:
                print("please try again")
                continue

        if(number <= 3):
            board[0][number-1] = value
        if(number >= 4 and number <= 6):
            board[1][number-4] = value
        if(number >= 7 and number <= 9):
            board[2][number-7] = value
        for i in board:
            print([i])    
       


    def check_win(board, value, player):
        
        win = False
       
        #check horizontals
        if (value == board[0][0] and value == board[0][1] and value == board[0][2]):
            print(player, "you WIN!!!")
            return True
            
                            
        if (value == board[1][0] and value == board[1][1] and value == board[1][2]):
            print(player, "you WIN!!!")
            return True
             
        if (value == board[2][0] and  value ==  board[2][1] and value == board[2][2]):
            print(player, "you WIN!!!")
            return True
             
        #check verticals
        if (value == board[0][0] and value == board[1][0] and value == board[2][0]):
            print(player, "you WIN!!!")
            return True
                 
        if (value == board[0][1] and value == board[1][1] and value == board[2][1]):
            print(player, "you WIN!!!")
            return True
             
        if (value == board[0][2] and value == board[1][2] and value == board[2][2]):
            print(player, "you WIN!!!")
            return True
             
        #check diagnals
        if (value == board[0][0] and value == board[1][1] and value == board[2][2]):
            print(player, "you WIN!!!")
            return True
             
        if (value == board[0][2] and value ==  board[1][1] and value == board[2][0]):
            print(player, "you WIN!!!")
            return True


game_board = [["1","2","3"],
              ["4","5","6"],
              ["7","8","9"]]


input_list = [1,2,3,4,5,6,7,8,9]

values = ["X","O"]

players = ["player_1","player_2"]

playing = True

game = Game(game_board, values[0], players[0], values[1], players[1])

game.start_game()














    

