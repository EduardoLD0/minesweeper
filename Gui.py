from Board import *
from graphics import *

# Graphical User Interface

class Gui:
    def __init__(self, width, height, tileSize, boardWidth, boardHeight, mineNum):
        self.win = GraphWin("Minesweeper", width, height)
        self.tileSize = tileSize
        self.board = Board(self.tileSize, boardWidth, boardHeight, mineNum)
        self.boardBorders = [10 + boardWidth * self.tileSize - 1, 10 + boardHeight * self.tileSize - 1]
        for i in self.board.getTiles():
            for j in i:
                j.getTex().draw(self.win)
        self.update()
    
    def update(self):
        exit = False
        while not exit:
            click = self.win.checkMouse() # Get click position
            # Check if the user clicked inside the board
            if click:
                if click.getX() > 10 and click.getX() < self.boardBorders[1]:
                    if click.getY() > 10 and click.getY() < self.boardBorders[0]:
                        queue = [click]
                        while len(queue) != 0:
                            currentClick = queue.pop()
                            [mine, number] = self.board.update(currentClick) # Update tile pressed
                            if not mine and number != None:
                                if number.getText() != "0":
                                    number.draw(self.win)
                            if number != None: # Reveal adjacent tiles if 0 near mines
                                if number.getText() == "0": # Reveal adjacent tiles if 0 near mines
                                    print("A")
                                    for i in range(-1, 2):
                                        for j in range(-1, 2):
                                            if not(i == 0 and j == 0):
                                                newClick = Point(currentClick.getX() + self.tileSize * i, currentClick.getY() + self.tileSize * j)
                                                if newClick.getX() > 10 and newClick.getX() < self.boardBorders[1]:
                                                    if newClick.getY() > 10 and newClick.getY() < self.boardBorders[0]:
                                                        queue.append(newClick)
            key = self.win.checkKey() # Get key from user
            if key == "Escape": # Escape key for exitting the program
                exit = True