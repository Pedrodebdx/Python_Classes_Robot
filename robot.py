class MonRobot:
    #class des robots
    robots_crees = 0
    def __init__(self, c_nom='sans nom', position="0,0", c_direction='0'):
        self.nom = c_nom
        self.position = position
        MonRobot.robots_crees +=1
        self.direction = c_direction

print("Création d'un robot !")
robot1 = MonRobot('nono le robot', '43 , 12')
print(f'Nom du robot 1: {robot2.nom }')
print(f'Sa postion est : {robot2.position }')
print(f'Nombres de robots crées :{MonRobot.robots_crees}')