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

class UnbeatableComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            spot = random.choice(game.available_moves())
        else:
            spot = self.minimax(game, self.letter)['position']
        return spot

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        # as the other player is also playing optimally, this will get executed
        # Assumption of Minimax Algorithm that both players are playing "optimally"
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_spots() + 1) if other_player == max_player else -1 * (
                        state.num_empty_spots() + 1)}
        #this elif condition can be commented out
        elif not state.empty_spots():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move #goes uptil next level and not full depth #recursion

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is the AI
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:                     # O is the AI
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

