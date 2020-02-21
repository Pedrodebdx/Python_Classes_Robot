"""
from robot import Robot

print("Création d'un robot !")
robot1 = Robot('C3PO')

print(' ---------------------------------------------------')
robot1.statut()

print(' ---------------------------------------------------')
print(' faisons AVANCER le robot')
robot1.avancer()
robot1.statut()

print(' ---------------------------------------------------')
print(' faisons TOURNER le robot')
robot1.tourner_droite()
robot1.statut()
print(' ---------------------------------------------------')
print(' faisons TOURNER le robot')
robot1.tourner_droite()
robot1.statut()
print(' ---------------------------------------------------')
print(' faisons AVANCER le robot')
robot1.avancer()
robot1.statut()
print(' ---------------------------------------------------')
print(' faisons AVANCER le robot')
robot1.avancer()
robot1.statut()
"""

from robot_ng import RobotNG
from robot import Robot

print("Création d'un robot !")
robot2 = RobotNG('Terminator')
print(' -----------------------INITIALISATION---------------------------')
robot2.statut()
print(' ---------------------- TURBO -----------------------------')
robot2.turbo()
robot2.statut()
print(' ---------------------- AVANCER_NG -----------------------------')
robot2.avancer_ng(12)
robot2.statut()

print(' ---------------------- DEMI-TOUR -----------------------------')
robot2.demi_tour()
robot2.statut()