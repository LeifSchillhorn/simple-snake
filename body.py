class Body:
    """_summary_
    """    
    def __init__(self,x,y,next,mapX,mapY) -> None:
        """initiate position next body part and map size

        Args:
            x (int): X position
            y (int): Y position
            next (Body): next Body part
            mapX (int): map size
            mapY (int): map size
        """        
        self.x = x
        self.y = y
        self.next = next
        self.mapX = mapX
        self.mapY = mapY
    
 
    def getNext(self):
        return self.next

    
    def getX(self)-> int:
        return self.x


    def getY(self)->int:
        return self.y

    def getList(self)->list:
        """generates a list of all positions of the bodyparts

        Returns:
            list: list of tupels of the positons for each body part
        """        
        if(not(self.next is None)):
            prev = self.next.getList()
            prev.append((self.x,self.y))
            return prev
        else:
            return[(self.x,self.y)]


    def changePos(self,newX,newY,lengthen,Nx,Ny)->None:
        """changes the position of all the body parts recursevly.

        Args:
            newX (int): the new position for this bodypart
            newY (int): new position for this bodypart
            lengthen (bool): if the snake has to lenghten by one when moving
            Nx (int): new head position
            Ny (int): new head position

        Raises:
            Exception: colision with itself.
        """        
        if(not(self.next is None)):
            if(self.x != Nx or self.y != Ny):
                self.next.changePos(self.x, self.y,lengthen,Nx,Ny)
            else:
                raise Exception('colision')
        elif lengthen:
            self.next = Body(self.x,self.y,None,self.mapX,self.mapY)
        self.x = newX
        self.y = newY

    def movesnake(self,newX,newY)->None:
        """move the snake to the coordinates with max manhaten distance of 1

        Args:
            newX (int): x position
            newY (int): y position
        """        
        if (abs(self.x - newX) + abs(self.y - newY) == 1):
                self.changePos(newX, newY, False, newX, newY)
        else:
            # raise Exception('Invalid new Position')
            pass
    

    def direct_move(self,direction,lengthen)->None:
        """moves in a cardinale direction, can move of the map

        Args:
            direction (str): direction of movment for the head ["n","e","s","w"]
            lengthen (bool): if the snake ate somthing and therfore gets longer.
        """        
        if direction == "e":
            mx = self.x + 1
            my = self.y
        if direction == "w":
            mx = self.x - 1
            my = self.y
        if direction == "n":
            mx = self.x 
            my = self.y + 1
        if direction == "s":
            mx = self.x 
            my = self.y - 1
        if(mx >= 0 and my >= 0 and mx <= self.mapX, my <= self.mapY):
            self.changePos(mx,my, lengthen, mx,my)
  
    def lengthen(self,newX,newY)->None:
        if (abs(self.x - newX) + abs(self.y - newY) == 1):
            self.changePos(newX, newY, True, newX, newY)
        else:
            raise Exception('Invalid new Position')