from utils import print_row_list, list_to_str, filter_match


class Board:
    def __init__(self):
        self.turn = 0
        self.game_result: str = ''
        self.rows: list[str] = []
        self.inline_board: str = '_' * 9
        self.render()

    strike_combinations = [
        # horizontal
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        # vertical
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        # cross
        [0, 4, 8],
        [2, 4, 6],
    ]

    @staticmethod
    def prepare_row(row: str) -> str:
        prepared_row = list(map(lambda char: f"{char} ", f"|{row}|"))
        return list_to_str(prepared_row)

    def render(self):
        row_count = int(len(self.inline_board) / 3)

        for i in range(row_count):
            start = i * 3
            row = str(self.inline_board[start:start + 3]).replace('_', ' ')
            self.rows.append(self.prepare_row(row))

        self.rows.insert(0, "---------")
        self.rows.append("---------")

        print_row_list(self.rows)
        self.rows = []

    def did_player_win(self, player: str):
        for combination in self.strike_combinations:
            strike = ''

            for position in combination:
                strike += self.inline_board[position]

            if strike == player * 3:
                return True

    def decide_who_wins(self):
        players = ['X', 'O']
        winners = list(filter(lambda p: self.did_player_win(p), players))

        if len(winners) > 0:
            self.game_result = f"{winners[0]} wins"
        elif self.is_finished():
            self.game_result = "Draw"

    def is_finished(self) -> bool:
        return self.game_result or self.turn == 9

    def is_free(self, target: int) -> bool:
        return self.inline_board[target] == '_'

    def make_move(self, target: int, player: str):
        exploded = list(self.inline_board)
        exploded[target] = player
        self.inline_board = str().join(exploded)
        self.turn += 1

    def update(self, target: int, player: str):
        if not self.is_free(target):
            raise LookupError

        self.make_move(target, player)

        self.render()

        if self.turn > 4:
            self.decide_who_wins()

            if self.is_finished():
                print(self.game_result)
