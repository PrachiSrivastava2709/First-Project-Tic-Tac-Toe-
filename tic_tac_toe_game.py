import random
class Player:
    
    def __init__(self, letter):
        #letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    #Single level Inheritance
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        spot = random.choice(game.available_moves())
        return spot

class UserPlayer(Player):
    #Single level Inheritance
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_spot = False
        spot = None
        while not valid_spot:
            spot = input(self.letter + "\'s move. Input move (0 - 8): ")
            try:
                valid_spot = int(spot)
                if valid_spot not in game.available_moves():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print("Invalid Spot. Enter Again")

        return spot



