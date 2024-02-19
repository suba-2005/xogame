import random

class UniqueTicTacToe:

    def __init__(self):
        self.play_area = []

    def setup_play_area(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.play_area.append(row)

    def choose_first_player(self):
        return random.randint(0, 1)

    def occupy_position(self, row, col, player):
        self.play_area[row][col] = player

    def check_player_win(self, player):
        win = None

        size = len(self.play_area)

        # Check rows
        for i in range(size):
            win = True
            for j in range(size):
                if self.play_area[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # Check columns
        for i in range(size):
            win = True
            for j in range(size):
                if self.play_area[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # Check diagonals
        win = True
        for i in range(size):
            if self.play_area[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(size):
            if self.play_area[i][size - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_full(self):
        for row in self.play_area:
            for item in row:
                if item == '-':
                    return False
        return True

    def switch_player(self, player):
        return 'X' if player == 'O' else 'O'

    def display_board(self):
        for row in self.play_area:
            for item in row:
                print(item, end=" ")
            print()

    def begin_game(self):
        self.setup_play_area()

        player = 'X' if self.choose_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.display_board()

            # Take user input
            row, col = list(
                map(int, input("Enter row and column numbers to occupy spot: ").split()))
            print()

            # Occupy the spot
            self.occupy_position(row - 1, col - 1, player)

            # Check if current player wins
            if self.check_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # Check if the game is a draw
            if self.is_board_full():
                print("Match Draw!")
                break

            # Switch player
            player = self.switch_player(player)

        # Show the final board
        print()
        self.display_board()

# Starting the game
tic_tac_toe = UniqueTicTacToe()
tic_tac_toe.begin_game()
