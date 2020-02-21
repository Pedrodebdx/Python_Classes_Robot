from robot import Robot


class RobotNG(Robot):
    
    def __init__(self, nom):
        super().__init__(nom)
        self.turbo = True
        
        
        
    def avancer(self, nombre_de_pas):
        if self.turbo == True:
            nombre_de_pas*=3
            print('mod turbo... ACTIVé !!!')
            
        for i in range(nombre_de_pas):
            super().avance()
        print('javance de {}'.format(nombre_de_pas))
        
      
    def gauche(self):
        super().droite()
        super().droite()
        super().droite()
        print('atttention je tourne à gauche ')

    def demi_tour(self):
        self.droite()
        self.droite()
        print('demi-tour les amis !')

    def turbo(self):
        if self.turbo == True:
            self.turbo = False
        else:
            self.turbo = True

    def etatng(self):
        super().etat()
        if self.turbo==True:
            print("le robot est en mode turbo")
        elif self.turbo==False:
            print("le robot n est pas en mode turbo")