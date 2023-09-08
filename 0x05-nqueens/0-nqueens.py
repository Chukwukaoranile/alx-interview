#!/usr/bin/python3
""" N queens Module """
import sys


class Chess:
    """ Chess object to nqueens problem
    """

    SOLUTIONS = []

    def __init__(self, N: int) -> None:
        """ Instance method

        Args:
            N (int): Chess board size
        """
        self.N = N
        # set up board
        self.board = [[0] * self.N for _ in range(self.N)]

    def is_safe(self, board, row: int, col: int, N) -> bool:
        """ Check if queen is safe for placement

        Args:
            board (List[list]): 2D chess board
            row (int): row inspecting
            col (int): col inspecting
            N (_type_): Board size

        Returns:
            bool: True if safe else false
        """
        # rule for checking if queens in the same row
        for i in range(col):
            if board[row][i] == 1:
                return False

        # rule for checking if queen is up
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # check if queen is down
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def find_solution(
            self, board,
            col: int, N: int, solutions) -> bool:
        """ find solution for nqueens problem

        Args:
            board (List[list]): 2D chess board
            col (int): column exploring
            N (int): board size
            solutions (List[list]): list of solution list

        Returns:
            bool: True if found else False
        """
        # found a solution meaning queens ain't attacking eachother
        if col >= N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        res = False
        for i in range(N):
            # backtracking meaning go back and undo if a spot isn't safe
            if self.is_safe(board, i, col, self.N):
                board[i][col] = 1
                # keep record of last valid solution if
                # there is no point moving forward
                res = self.find_solution(
                    board, col + 1, self.N, solutions) or res
                # undo temporary placement
                board[i][col] = 0

        return res

    def solve_nqueens(self) -> None:
        """ N queens method
        """
        # if no valid solution is found return empty list
        if not self.find_solution(self.board, 0, self.N, Chess.SOLUTIONS):
            return []

        return Chess.SOLUTIONS


def main() -> None:
    """ main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens: Chess = Chess(N)
    solutions = nqueens.solve_nqueens()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
