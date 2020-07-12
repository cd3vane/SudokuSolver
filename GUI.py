import pygame
from sudokuSolver import solveBoard, isValidEntry
import time
pygame.font.init()


class Grid:
    sudokuBoard = [
             [5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    def __init__(self, rows, columns, width, height):
        self.rows = rows
        self.columns = columns
        self.cubes = [[Cube(self.board[i][j], i, j, width, height)
                      for j in range(columns)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)]
                      for i in range(self.rows)]

    def place(self, new_value):
        row, column = self.selected
        if self.cubes[row][column].value == 0:
            self.cubes[row][column].set(new_value)
            self.update_model()

            isValid = isValidEntry(self.model, new_value, (row, column))
            if isValid and solveBoard(self.model):
                return True
            else:
                self.cubes[row][column].set(0)
                self.cubes[row][column].set_temp(0)
                self.update_model
                return False

    def sketch(self, new_value):
        row, column = self.selected
        self.cubes[row][column].set_temp(new_value)




class Cube:
    rows = 9
    columns = 9

    def __init__(self, value, row, column, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        font = pygame.font("")


def redrawWindow(window, board, time, strikes):


def formatTime(seconds):
    second = seconds % 60
    minute = second // 60

    time_format = " " + str(minute) + ":" + str(second)
    return time_format


def main():
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0

    while run:
