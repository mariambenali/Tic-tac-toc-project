import os

def clean_system():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        name= input("Enter your name: ")
        self.name=name
        print("The name is correct!")

    def choose_symbol(self):
        while True:
            symbol= input(f"{self.name},Choose your symbol: ")
            if symbol.isalpha() and len(symbol) ==1 :
                self.symbol=symbol.upper()
                break
            print("The symbol is correct!") 


class Menu:
    def display_startgame(self):
        print("welcome to the game!")
        print("Tap 1. if you want to start the game!")
        print("Tap 2. if you want to quit the game!")
        number= input("Enter your number")
        return number
    
    def display_endgame(self):
        print("Game over")
        print("Try again")
        print("Quit the game")
        endgame= input("Enter your choice")
        return endgame
    
class Board:
    def __init__(self):
        self.board= [str(i) for i in range (1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print("|".join (self.board[i:i+3]))
            if i < 6:
                print("-"*5)
    def update_board(self,choice,symbol):
        if self.board(self,choice):
            self.board[choice-1]=symbol
            return True
        return False

    def empty_colon(self,choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board= [str(i) for i in range (1,10)]

class Game:
    def __init__(self):
        self.player=[Player(),Player()]
        self.menu= Menu()
        self.board=Board()
        self.current_player_index= 0

    def start_game(self):
        choice=self.menu.display_startgame()
        if choice == "1":
            self.enter_player()
            self.play_game()
        else:
            self.quit_game()

    def enter_player(self):
        for number,player in enumerate(self.player, start = 1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clean_system()
    
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice= self.menu.display_startgame()
                if choice == 1:
                    self.restart_game()
                else: 
                    self.quit_game()
                    break
    


    def play_turn(self):
        players = self.player[self.current_player_index]
        self.board.display_board()
        print(f"{Player.name}'s turn")
        while True:
            try:
                cell_choice= int(input("choose a cell from (1–9)"))
                if 1<= cell_choice <=9 and self.Board.update_board(cell_choice, players.symbol):
                    break
                else:
                    print("invalid!")
            except ValueError:
                print("please enter a number between 0 and 9")

        self.switch_player()
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    

    def check_win(self):
        win_combination = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for combo in win_combination:
            if(self.board.board[combo[0]]==self.board.board[combo[1]]==self.board.board[combo[2]]):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()

    def quit_game(self):
        print("Thank you!")



game= Game()
game.start_game()
game.play_game()