class Tile:
    
    def __init__(self):
        self.x = None
        self.y = None
        self.lev = None
        self.rover = None
        self.message = None
        self.has_rover = False
        self.has_message = False
        self.inspected = False
        pass
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, n):
        self.x = n
        return
    
    def setY(self, n):
        self.x = n
        return
    
    def getLev(self):
        return self.lev
    
    def setLev(self, n):
        self.lev = n
        return
    
    def setRover(self, r):
        self.rover = r
        return
    
    def getRover(self):
        return self.rover
    
    def getMessage(self):
        return this.message
    
    def setMessage(self, m):
        self.message = m
        return
    
    def hasMessage(self):
        return self.has_message
    
    def hasRover(self):
        return self.has_rover
    
    def messageSet(self):
        self.has_message = True
        return
    
    def roverSet(self):
        self.has_rover = True
        
        
        
    
