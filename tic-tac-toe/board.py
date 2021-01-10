from utils import print_row_list, list_to_str


class Board:
    def __init__(self):
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
