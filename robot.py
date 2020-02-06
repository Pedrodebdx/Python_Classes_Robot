class MonRobot:
    #class des robots
    robots_crees = 0
    def __init__(self, c_nom='sans nom', position_x="0", position_y="0", c_direction='0'):
        self.nom = c_nom
        self.position_x = position_x
        self.position_y = position_y
        MonRobot.robots_crees +=1
        self.direction = c_direction


    def avancer(self, avance):
        if avance == "Est" :
            self.position_x += 1
        if avance == "Nord":
            self.position_y += 1

    def tourner(self, tourne):
        print('tourne à gauche marcel')

print("Création d'un robot !")
robot1 = MonRobot('nono le robot', '43' , '12')
print(f'Nom du robot 1: {robot1.nom }')
print(f'Sa postion est : {robot1.position_x}, {robot1.position_y}')
print(f'Nombres de robots crées :{MonRobot.robots_crees}')