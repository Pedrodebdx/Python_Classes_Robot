from robot import Robot
from robotNG import RobotNG

print('-----Avance-------')
robotng1 = RobotNG('Ivanka')
robotng1.avance()
robotng1.avance()
robotng1.avance()
robotng1.etat()

print('------avancer (5)------')
robotng1.avancer(20)
robotng1.etat()

print('------gauche------')
robotng1.gauche()
robotng1.etat()

print('------Droite------')
robotng1.droite()
robotng1.etat()

print('------avancer (5)------')
robotng1.avancer(20)
robotng1.etat()

print('------demi-tour------')
robotng1.demi_tour()
robotng1.etatng()
robotng1.etat()