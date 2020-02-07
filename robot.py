class Robot:
    #class des robots
    
    def __init__(self, c_nom='inconnu' ,x=0,y=0, c_direction='Est'):
        self.nom = c_nom
        self.position_x = x
        self.position_y = y
        self.direction = c_direction

    def statut(self):
        print(f'Je suis: {self.nom}')
        print(f'ma postion est : {self.position_x}, {self.position_y}')
        print(f'je suis en direction de : {self.direction}')

    def avancer(self):
        if self.direction == "Est" :
            self.position_x += 1
        elif self.direction == "Nord":
            self.position_y += 1
        elif self.direction == "Sud":
            self.position_y -= 1  
        elif self.direction == "Ouest" :
            self.position_x -= 1 

    def tourner_droite(self):
        if self.direction == 'Est':
            self.direction = 'Sud'
        elif self.direction == 'Sud':
            self.direction = 'Ouest'
        elif self.direction == 'Ouest':
            self.direction = 'Nord'
        elif self.direction == 'Nord':
            self.direction = 'Est'
       