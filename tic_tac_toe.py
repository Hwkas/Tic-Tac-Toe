import pandas as pd


class TicTacToe():
    def __init__(self):
        """
        This class is about the game Tic Tac Toe.\n
        Attirbuted -
            |self.array - which contains the array.|                                
            |self.game_complete - if True means the game over, False means vice-versa.|
        """
        self.array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.game_complete = False
        print(pd.DataFrame(self.array))

    def turn(self, loc, marker):
        """
        This method check & implements the turn of the player.\n
        Arguments - 
            |loc - location at which you want to put element in the array.|
            |marker - player mark 'X' or 'O'.|
        |return True if the move was valid, else return False
        """
        loc[0] = int(loc[0])
        loc[1] = int(loc[1])
        if (loc[0] >= 0 and loc[0] <= 2) and (loc[1] >= 0 and loc[1] <= 2):
            if self.array[loc[0]][loc[1]] == " ":
                self.array[loc[0]][loc[1]] = marker
                print(pd.DataFrame(self.array))
                return True
            else:
                print("\nThis block is already used, please re-enter for another block location.\n")
                print(pd.DataFrame(self.array))
                return False
        else:
            print("\nInvalid block, Please choose a valid block from range '0-2' both for x-axis & y-axis.\n")  
            print(pd.DataFrame(self.array))          
            return False

    def game_over(self):
        """
        This method check if the game completed like all the codition for winnig the game or Draw.
        |return True if game completed , else return False|
        """
        for i in range(0, 3):
            if self.array[i][0] == self.array[i][1] and self.array[i][1] == self.array[i][2] and self.array[i][1] != " ":
                print(f"\nPlayer '{self.array[i][1]}' won!\n")
                print(pd.DataFrame(self.array))
                self.game_complete = True   
                return True
            elif self.array[0][i] == self.array[1][i] and self.array[1][i] == self.array[2][i] and self.array[1][i] != " ":
                print(f"\nPlayer '{self.array[1][i]}' won!\n")
                print(pd.DataFrame(self.array))
                self.game_complete = True
                return True
        if self.array[0][0] == self.array[1][1] and self.array[1][1] == self.array[2][2] and self.array[1][1] != " ":
            print(f"\nPlayer '{self.array[1][1]}' won!\n")
            print(pd.DataFrame(self.array))
            self.game_complete = True
            return True
        elif self.array[0][2] == self.array[1][1] and self.array[1][1] == self.array[2][0] and self.array[1][1] != " ":
            print(f"\nPlayer '{self.array[1][1]}' won!\n")
            print(pd.DataFrame(self.array))
            self.game_complete = True
            return True
        elif self.array[0][0] != " " and self.array[0][1] != " " and self.array[0][2] != " " and self.array[1][0] != " " and self.array[1][1] != " " and self.array[1][2] != " " and self.array[2][0] != " " and self.array[2][1] != " " and self.array[2][2] != " ":
            print(f"\nIt's a Draw!\n")
            self.game_complete = True
            return True
        else: 
            return False