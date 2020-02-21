class Robot():
    """ cette classe créee les robots"""
    
    def __init__(self, nom, position_x=0, position_y=0, direction="Est"):
        self.nom = nom
        self.position_x = position_x
        self.position_y = position_y
        self.direction = direction
        
    def avance(self):
        
        if self.direction == "Est":
            self.position_x += 1
        elif self.direction == "Ouest":
            self.position_x -= 1
        elif self.direction == "Nord":
            self.position_y += 1
        elif self.direction == "Sud":
            self.position_x -= 1    
        
    def droite(self):
        
        if self.direction == "Est":
            self.direction = "Sud"
        elif self.direction == "Sud":
            self.direction = "Ouest"
        elif self.direction == "Ouest":
            self.direction = "Nord"
        elif self.direction == "Nord":
            self.direction = "Est"
            
    def etat(self):
        print("Je m'appelle {}".format(self.nom))
        print("Je marche dans la direction {}".format(self.direction))
        print("ma position x est {} et ma position y est {}".format(self.position_x, self.position_y))
        
        
        
        


