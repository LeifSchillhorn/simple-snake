
import random
import body



class Snake:
    """_summary_
    """    
    def __init__(self, mapX=10,mapY=10,startlength=4,groth=True)->None:
        """_summary_

        Args:
            mapX (int, optional): _description_. Defaults to 10.
            mapY (int, optional): _description_. Defaults to 10.
            startlength (int, optional): _description_. Defaults to 4.
            groth (bool, optional): _description_. Defaults to True.
        """        
        self.mapX = mapX
        self.mapY = mapY
        self.length = startlength
        self.body = body.Body(0,0,None,self.mapX,self.mapY)
        for l in range(1,self.length):
            self.body = body.Body(0,l,self.body,self.mapX,self.mapY)
        self.fruitX = random.randint(1, self.mapX -1)
        self.fruitY = random.randint(1, self.mapY -1)
        self.score = 0
        self.groth = groth
    
    def step(self,direction) -> int:
        """_summary_

        Args:
            direction (_type_): _description_

        Returns:
            int: _description_
        """        
        try:
            if(self.body.getX() == self.fruitX and self.body.getY() == self.fruitY):
                if self.groth:
                    self.body.direct_move(direction, True) 
                else:
                    self.body.direct_move(direction, False) 
                while ((self.fruitX, self.fruitY) not in self.body.getList()):
                    self.fruitX = random.randint(1, self.mapX -1)
                    self.fruitY = random.randint(1, self.mapY -1)
            else:
                self.body.direct_move(direction, False)
            return 0
        except Exception as inst:
            if (inst.args == "colision"):
                return -1
            
    def getState(self):
        """_summary_
        """
        self.body.getList()
        self.score
        self.fruitX
        self.fruitY

