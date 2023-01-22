# Class Tile
# Contains:
# 2 points for the size of the tile
# A boolean value indicating if it has a mine or not
# A texture

class Tile:
    def __init__(self, p1, p2, isMine, tex):
        self.p1 = p1
        self.p2 = p2
        self.isMine = isMine
        self.tex = tex
        self.visited = False
  
    def getIsMine(self):
        return self.isMine
    
    def setIsMine(self, isMine):
        self.isMine = isMine
    
    def getTex(self):
        return self.tex
    
    def setTex(self, tex):
        self.tex = tex
    
    def getVisited(self):
        return self.visited
    
    def setVisited(self, visited):
        self.visited = visited