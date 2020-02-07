from robot import Robot
class RobotNG(Robot):
    
    def __init__(self,c_nom='inconnu', option=False):
        super().__init__(c_nom)
        self.option=False

    def statut(self):
        Robot.statut(self)
        print(f'Mode turbo: {self.option}')
        


    def turbo(self):
        if self.option==False:
            self.option=True
        else :
            self.option=False
 
    def avancer_ng(self,nbre_de_pas):
        for i in range(nbre_de_pas):
            Robot.avancer(self)