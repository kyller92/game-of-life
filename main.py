"""
    Main File
"""
from grid import Grid

def main():
    grid = Grid(9,9)
    print(grid.showGrid())
    grid.startPosition()


if __name__ == '__main__':
    main()