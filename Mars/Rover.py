class Rover:
    def __init__(self):
        self.x = None
        self.y = None
        self.lev = None
        self.location = None
        self.explored = 0
        pass
    
    def getX(self):
        return self.x
    
    def setX(self, val):
        self.x = val
        return
    
    def getY(self):
        return self.y
    
    def getLev(self):
        return self.lev
    
    def setLev(self, n):
        self.lev = n
        return
    
    def setY(self, val):
        self.y = val
        return
    
    def setPos(self, pos):
        self.location = pos
        return
    
    def getPos(self):
        return self.location
        
        
    
        
    
        
