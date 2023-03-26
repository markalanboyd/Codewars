import boards

KING = '♔'
PAWN = '♟'
BISHOP = '♝'

# Functions
def parse_board(example: dict) -> list:
    return example["board"]

def get_coordinates(example_board: list, piece: str) -> tuple:
    for i, row in enumerate(example_board):
        if piece in row:
            return (i, row.index(piece))
    return None

def pawn_check(board: list) -> bool:
    for row in board:
        if PAWN not in row:
            continue
        pawn_row = board.index(row)
        next_row = board[pawn_row + 1]
        if KING not in next_row:
            continue
        pawn_index = row.index(PAWN)
        king_index = next_row.index(KING)
        return king_index == (pawn_index - 1) or king_index == (pawn_index + 1)
    return False

def bishop_check(board: list) -> bool:
    king_coord = get_coordinates(board, KING)
    bishop_coord = get_coordinates(board, BISHOP)
    # (Row, Col)
    # .....  (0, 5), (0, 7)
    # Bishop (1, 6)
    # .....  (2, 5), (2, 7)
    # King (7, 0)
    king_row = king_coord[0]
    king_col = king_coord[1]
    bishop_row = bishop_coord[0]
    bishop_col = bishop_coord[1]
    
    if king_row == bishop_row or king_col == bishop_col:
        return False
    
        
    
    
        
        

                
def is_king_in_check(chessboard: iter) -> bool:
    pawn = next(chessboard)
    pawn_board = parse_board(pawn)
    print(pawn_check(pawn_board))
    
    bishop = next(chessboard)
    bishop_board = parse_board(bishop)
    print(bishop_check(bishop_board))

def main() -> None:
    is_king_in_check(boards.ITER)

# Main
if __name__ == "__main__":
    main()
