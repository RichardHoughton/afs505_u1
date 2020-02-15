"""A Python script that runs Conway's Game of Life.


.. module:: Project01
    :platform: Windows
    :synopsis: This script plays Conway's Game of Life within a 30x80 matrix.
    It will play for as many ticks as instructed by the input in the command line.

.. moduleauthor:: Richard B. Houghton richard.houghton@wsu.edu
.. modulereviewer: Greysen W. Danae greysen.danae@wsu.edu
"""

# reviewer score 100/100, I took the liberty of changing a few typos
# code runs perfectly with specified command line arguments


from sys import argv

def init_grid(grid, cell_indexes):
    """Turns cells from 0s to 1s inside the original grid.

    :param grid: dimensions of the martix
    :param cell_indexes: the row and column of each cell index
    :type grid: list
    :type cell_indexes: string

    :return: a 30x80 matrix with all active cells representing
    as 1s
    :rtype: a list with 2400 elements with certain elements showing as 1s

    """
# reviewer edited frm to from in above description

    for active in cell_indexes:
        i, j = active.split(":") # splits any numbers with a colon in between them
        grid[int(i) - 1][int(j) - 1] = 1

def print_grid(grid, n, m):
    """creates a 30x80 matrix and then changes all the 0s and 1s to dashes
       and Xs, while preserving the numerical values

    :param grid: dimensions of the martix
    :param n: an integer
    :param m: an integer
    :type grid: string
    :type n: int
    :type m: int

    :return: grid of dashes and Xs depending on command line input
    :rtype: list of 2400 elements of dashes and Xs
    """

# edited by reviewer: type n and m were written as :param n/m: instead of :type n/m:
    for i in range(n - 1):
        for j in range(m - 1):
            if grid[i][j] == 1: print("X", end = "")
            if grid[i][j] == 0: print("-", end = "")
        print() #prints the X's and dashes
    print() #prints the grid as a whole


def play_game(grid, n, m):
    """Creates a new grid with all 0s, then runs the rules of the Game of Life
       and returns that grid.

    :param grid: dimensions of the martix
    :param n: an integer
    :param m: an integer
    :type grid: string
    :type n: int
    :type m: int

    :return: grid of dashes and Xs depending on command line input
    :rtype: list of 2400 elements of dashes and Xs
    """

# edited by reviewer: type n and m were written as :param n/m: instead of :type n/m:

    new_grid = [[0] * m for i in range(n)] #creates a new grid full of zeros
    for i in range(n - 1):
        for j in range(m - 1):
            neighbors = int(grid[i - 1][j - 1]) + \
             int(grid[i][j - 1]) + int(grid[i + 1][j - 1]) + int(grid[i - 1][j]) + \
             int(grid[i + 1][j]) + int(grid[i - 1][j + 1]) + int(grid[i][j + 1]) + \
             int(grid[i + 1][j + 1]) # sums the neighbors of all the cells around a specific cell
            if grid[i][j] == 1 and neighbors < 2:
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and neighbors == 2:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbors == 3:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbors > 3:
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    return(new_grid)

def main(argv):
    """ Reads inputs from the command line and runs the code.

    :param argv: argument vector
    :type argv: list

    :return: nothing
    :rtype: nothing

    """
    script = argv[0] # calls the script name
    ticks = int(argv[1]) # number of cycles the program will go through
    cell_indexes = argv[2:] # cell indexes that will become active
    n = 31 # number of rows
    m = 81 # number of columns
    grid = [[0] * m for i in range(n)] # creates a grid full of zeroes
    tick = 0 #number of ticks gone through

    init_grid(grid, cell_indexes)
    print_grid(grid, n, m)
    while ticks > tick:
        grid = play_game(grid, n, m) # plays games and then saves result as grid
        print_grid(grid, n, m)
        tick += 1



if __name__ == "__main__":
    main(argv)
