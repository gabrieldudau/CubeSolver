#!/usr/bin/env pybricks-micropython

import copy
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from Robot.Cube.Cube import Wuerfel
from Robot.Cube.CubeSolver import CubeSolver
from Robot.Sensors.Farbchecker import Farbchecker

from Robot.Robot import Robot

# -----------------------------------------------------------------Testprogramm für PC ohne ev3-----------------------------------------------------------------

farb = Farbchecker()
wurf = Wuerfel()
solve = CubeSolver(wurf, True)


# Dieser moveset hat Mal für Bugs gesorgt. Mit diesen Zeilen kann man gut testen. 

"""
moveset = [('Y', -1), ('Y', 1), ('O', 1), ('B', -1), ('B', -1), ('G', -1), ('G', -1), ('R', 1), ('G', 1), ('O', 1)]
for item in moveset:
    wurf.seiteDrehen(item[0], item[1])
"""

"""
print(wurf.colorPrint())

mix = [('B', 1), ('B', 1), ('B', 1), ('W', 1), ('R', -1), ('Y', 1), ('W', 1), ('G', -1), ('Y', -1), ('Y', 1)]

for item in mix:
    wurf.seiteDrehen(item[0], item[1])

print(wurf.colorPrint())

solve = [('O', 1), ('Y', 1), ('O', 1), ('B', 1), ('B', 1), ('R', 1), ('R', 1), ('Y', -1), ('Y', -1), ('G', 1), ('G', 1), ('B', 1), ('B', 1), ('R', 1), ('R', 1), ('O', 1), ('O', 1), ('Y', -1), ('Y', -1), ('Y', -1), ('O', 1), ('Y', 1), ('O', -1), ('Y', -1), ('O', 1), ('Y', 1), ('O', -1), ('Y', -1), ('O', 1), ('Y', 1), ('O', -1), ('Y', -1), ('B', 1), ('Y', 1), ('B', -1), ('Y', -1), ('B', 1), ('Y', 1), ('B', -1), ('Y', -1), ('Y', 1), ('G', 1), ('Y', -1), ('G', -1), ('Y', -1), ('R', 1), ('Y', 1), ('R', -1), ('Y', -1), ('Y', -1), ('Y', 1), ('B', 1), ('Y', 1), ('B', -1), ('Y', -1), ('O', -1), ('Y', -1), ('O', 1), ('Y', 1), ('Y', -1), ('Y', -1), ('Y', 1), ('O', 1), ('Y', 1), ('O', -1), ('Y', -1), ('G', -1), ('Y', -1), ('G', 1), ('Y', 1), ('R', 1), ('Y', 1), ('R', -1), ('Y', -1), ('B', -1), ('Y', -1), ('B', 1), ('Y', 1), ('Y', -1), ('Y', -1), ('R', -1), ('Y', -1), ('R', 1), ('Y', 1), ('G', 1), ('Y', 1), ('G', -1), ('Y', -1), ('Y', -1), ('B', -1), ('Y', -1), ('B', 1), ('Y', 1), ('R', 1), ('Y', 1), ('R', -1), ('Y', -1), ('B', 1), ('R', 1), ('Y', 1), ('R', -1), ('Y', -1), ('B', -1), ('G', 1), ('O', 1), ('Y', 1), ('O', -1), ('Y', -1), ('G', -1), ('G', 1), ('G', 1), ('G', -1), ('Y', 1), ('G', 1), ('Y', 1), ('Y', 1), ('G', -1), ('B', -1), ('O', 1), ('B', -1), ('R', 1), ('R', 1), ('B', 1), ('O', -1), ('B', -1), ('R', 1), ('R', 1), ('B', 1), ('B', 1), ('R', -1), ('B', 1), ('R', -1), ('G', 1), ('G', 1), ('R', 1), ('B', -1), ('R', -1), ('G', 1), ('G', 1), ('R', 1), ('R', 1), ('G', 1), ('Y', -1), ('G', 1), ('Y', 1), ('G', 1), ('Y', 1), ('G', 1), ('Y', -1), ('G', -1), ('Y', -1), ('G', 1), ('G', 1), ('G', 1), ('Y', -1), ('G', 1), ('Y', 1), ('G', 1), ('Y', 1), ('G', 1), ('Y', -1), ('G', -1), ('Y', -1), ('G', 1), ('G', 1), ('Y', 1)]

for item in solve:
    wurf.seiteDrehen(item[0], item[1])

print(wurf.colorPrint())
"""

wurf.mischen(10)

mix = copy.deepcopy(wurf.getCubeHistory())


solve.solveCube()


solved = copy.deepcopy(solve.getHistory())


print("\n\n\n\n")

test = Wuerfel()

for item in mix:
    test.seiteDrehen(item[0], item[1])
    
print("_"*150 + "\n" + "_"*150 + "\n\n\nTest des Lösungsweges:\n\n\n" + "_"*150+"\n" + "_"*150+"\n\nNeuer Testwürfel:\n\n")
print(test.colorPrint())
print("_"*150 + "\n" + "_"*150 + "\n\n\nLoesefolge:\n\n\n" + str(solved) + "\n\n" + "Es wurden "+ str(len(solved)) + " Umdrehungen gebracht!\n\n")

for item in solved:
    test.seiteDrehen(item[0], item[1])

print(wurf.colorPrint())






"""
So wird ein Würfel erzeugt, indem man die Farben manuell eingibt. 
print(Wuerfel({"R": ["G","G","G","G","G","G","G","G"],
               "Y": ["G","G","G","G","G","G","G","G"],
               "O": ["G","G","G","G","G","G","G","G"],
               "W": ["G","G","G","G","G","G","G","G"],
               "B": ["G","G","G","G","G","G","G","G"],
               "G": ["G","G","G","G","G","G","G","G"]}).colorPrint())

check = Wuerfel()
check.setFarbenFuerSeite("R", 1, "G")
print(check.colorPrint())

"""

