import boards

KING_SYMBOL = '♔'
PAWN_SYMBOL = '♟'

# Functions
def parse_board(example_board: dict) -> list:
    return example_board["board"]

def pawn_check(board: list) -> bool:
    for row in board:
        if PAWN_SYMBOL in row:
            pawn_row = board.index(row)
            next_row = board[pawn_row + 1]
            if KING_SYMBOL in next_row:
                pawn_index = row.index(PAWN_SYMBOL)
                king_index = next_row.index(KING_SYMBOL)
                if king_index == (pawn_index - 1) or king_index == (pawn_index + 1):
                    return True
                else:
                    return False
                
def is_king_in_check(chessboard: iter) -> bool:
    pawn = next(chessboard)
    pawn_board = parse_board(pawn)
    print(pawn_check(pawn_board))

def main() -> None:
    is_king_in_check(boards.ITER)

# Main
if __name__ == "__main__":
    main()
