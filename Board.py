from Tile import *
from graphics import *
from random import randint as rand

class Board:
    def __init__(self, tileSize, width, height, mineNum):
        self.tileSize = tileSize
        self.width = width
        self.height = height
        self.mineNum = mineNum
        self.tiles = self.generateTiles()

    def generateTiles(self):
        tiles = []
        for i in range(self.width): # Generate matrix of empty tiles
            row = []
            for j in range(self.height):
                # Each point is adjusted according to the tileSize, there's no overlapping
                p1 = Point(10 + j * self.tileSize, 10 + i * self.tileSize)
                p2 = Point(10 + self.tileSize - 1 + j * self.tileSize, 10 + self.tileSize - 1 + i * self.tileSize)
                tex = Rectangle(p1, p2)
                tex.setFill(color_rgb(150, 150, 255))
                row.append(Tile(p1, p2, False, tex))
            tiles.append(row)
        # Generate mines
        i = 0
        while i < self.mineNum:
            tile = tiles[rand(0, self.width - 1)][rand(0, self.height - 1)]
            if tile.getIsMine() == False:
                tile.setIsMine(True)
                i += 1
            print(i)

        return tiles

    def update(self, click):
        # Get tile where user clicked
        row = int((click.getY() - 10) // self.tileSize)
        column = int((click.getX() - 10) // self.tileSize)
        tile = self.tiles[row][column]
        # Check if tile is visited
        if tile.getVisited() == True:
            return [False, None]
        if tile.getIsMine() == True: # If the tile contains a mine
            fill = "red"
            mine = True
            number = None
        else: # If the tile is empty
            fill = color_rgb(200, 200, 255)
            mine = False
            number = Text(Point(20 + column * self.tileSize, 20 + row * self.tileSize), str(self.searchMines(row, column)))
        # Change tile texture
        tex = tile.getTex()
        tex.setFill(fill)
        tile.setVisited(True)
        return [mine, number]
    
    def searchMines(self, row, column):
        mineCount = 0
        # Corners
        left = row - 1
        right = row + 1
        up = column - 1
        down = column + 1
        # Check for positions outside the board
        if left < 0:
            left = 0
        if right >= self.width:
            right = self.width - 1
        if up < 0:
            up = 0
        if down >= self.height:
            down = self.height - 1
        for i in range(left, right + 1):
            for j in range(up, down + 1):
                if self.tiles[i][j].getIsMine() == True:
                    mineCount += 1
        return mineCount

    def getTiles(self):
        return self.tiles