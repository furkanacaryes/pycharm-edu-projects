from board import Board
from utils import assert_every, assert_any, filter_match, str_to_int_list


class TicTacToe:
    def __init__(self):
        self.turn = 0
        self.game_result: str = ''
        self.board: Board = Board()
        self.play()

    coordinates: list[int]
    player = 'X'

    def switch_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def coords_to_index(self) -> int:
        [y, x] = self.coordinates  # vertical-first
        return (y - 1) * 3 + x - 1

    def are_all_in_range(self):
        if not assert_every(lambda c: 0 < c <= 3, self.coordinates):
            raise AssertionError

    def input_safely(self) -> int:
        user_coordinates = input("Enter the coordinates:")
        self.coordinates = str_to_int_list(user_coordinates)
        self.are_all_in_range()
        return self.coords_to_index()

    def does_combination_match(self, combination: list[int]) -> bool:
        return assert_every(lambda position: self.board.inline_board[position] == self.player, combination)

    def did_player_win(self):
        return assert_any(self.does_combination_match, self.board.strike_combinations)

    def decide_who_wins(self):
        did_win = self.did_player_win()

        if did_win:
            self.game_result = f"🎉 '{self.player}' WON!"
        elif self.is_finished():
            self.game_result = "💥 Draw"
        else:
            print('still playing')

    def is_finished(self) -> bool:
        return self.game_result or self.turn == 9

    def is_free(self, target: int) -> bool:
        return self.board.inline_board[target] == '_'

    def make_move(self, target: int):
        exploded = list(self.board.inline_board)
        exploded[target] = self.player
        self.board.inline_board = str().join(exploded)
        self.turn += 1

    def update(self, target: int):
        if not self.is_free(target):
            raise LookupError

        self.make_move(target)

        self.board.render()

        if self.turn > 4:
            self.decide_who_wins()

            if self.is_finished():
                print(self.game_result)

    def play(self):
        try:
            move = self.input_safely()
            self.update(move)
        except ValueError:
            print('You should enter numbers!')
        except AssertionError:
            print('Coordinates should be from 1 to 3!')
        except LookupError:
            print('This cell is occupied! Choose another one!')
        else:
            self.switch_player()
        finally:
            if not self.is_finished():
                self.play()


TicTacToe()
