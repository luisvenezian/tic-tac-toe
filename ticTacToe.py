import math
import tkinter as tk
    
    
class TicTacToe:
    def __init__(self):
        self.state = [None] * 9
        self.machine = 'X'
    
    def actions(self, s: list) -> list:
        # Returns legal moves in this given state (s)
        return [i for i, mark in enumerate(s) if mark is None]

    def player(self, s: list) -> str:
        # Returns which player to move in the given state (s)
        return 'X' if s.count(None) % 2 == 1 else 'O'

    def result(self, s: list, a: int, commit: bool = False) -> list:
        # Returns a state after action (a) taken in state (s)
        p = self.player(s)
        state = s.copy()
        state[a] = p
        
        if commit:
            self.state = state
            
        return state

    def terminal(self, s: list):
        # Checks if state (s) is a terminal state
        return True if self.utility(s) else False
                
    def utility(self, s: list) -> int:
        # takes the state and returns a numeric value
        # if x wins 1
        # if o wins -1
        # if draw 0
        # if game is not over None
        
        # Checking winning case
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
            [0, 4, 8], [2, 4, 6]             # diagonal
        ]
        for combo in winning_combos:
            if (s[combo[0]] is not None and
                s[combo[0]] == s[combo[1]] and
                s[combo[1]] == s[combo[2]]):
                return 1 if s[combo[0]] == 'X' else -1
            
        # Checking draw case
        if None not in s:
            return 0
        
        # Game is not over
        return

    def max_value(self, s: list) -> int:
        if self.terminal(s):
            return self.utility(s)
        v = -math.inf
        for a in self.actions(s):
            v = max(v, self.min_value(self.result(s, a)))
        return v

    def min_value(self, s: list) -> int:
        if self.terminal(s):
            return self.utility(s)
        v = math.inf
        for a in self.actions(s):
            v = min(v, self.max_value(self.result(s, a)))
        return v
    
    def machine_move(self, s: list) -> int:
        v = -math.inf
        for a in self.actions(s):
            t = self.min_value(self.result(s, a))
            if t > v:
                v = t
                action = a
        return action


# create visual board
def create_board(game: TicTacToe, start: str = 'X'):
    for i in range(3):
        for j in range(3):
            button = tk.Button(
                window, 
                text="", 
                font=("Arial", 50), 
                height=2, 
                width=6, 
                bg="lightblue", 
                command=lambda 
                row=i, 
                col=j: action(game, row, col, player=game.player(game.state))
            )
            button.grid(row=i, column=j, sticky="nsew")
            
    if start == game.machine:
        machine_turn(game)

def machine_turn(game: TicTacToe):
    move = game.machine_move(game.state)
    row, col = move // 3, move % 3
    action(game, row, col, game.machine) 
    
    
def action(game: TicTacToe, row: int, col: int, player: str):
    move = row * 3 + col
    
    if not game.state[move] or player == game.machine:     
        # update state
        game.result(game.state, move, commit=True)
        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=game.state[move])
        
    if game.terminal(game.state):
        result = game.utility(game.state)
        
        # print 
        if result == 1:
            print("X wins")
        elif result == -1:
            print("O wins")
        else:
            print("Draw")
    
    elif player != game.machine:
        machine_turn(game)
    
    
    
if __name__ == '__main__':    
    ticTacToe = TicTacToe()
    window = tk.Tk()
    window.title("Tic Tac Toe")
    create_board(ticTacToe)
    window.mainloop()
    
    
    