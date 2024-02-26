#!/usr/bin/env pybricks-micropython

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

# -----------------------------------------------------------------Testprogramm für PC ohne ev3-----------------------------------------------------------------




# Dieser moveset hat Mal für Bugs gesorgt. Mit diesen Zeilen kann man gut testen. 

"""
moveset = [('Y', -1), ('Y', 1), ('O', 1), ('B', -1), ('B', -1), ('G', -1), ('G', -1), ('R', 1), ('G', 1), ('O', 1)]
for item in moveset:
    wurf.seiteDrehen(item[0], item[1])
"""

"""
mix = [('W', -1), ('O', -1), ('W', 1), ('G', 1), ('W', -1), ('B', -1), ('G', 1), ('B', 1), ('W', 1), ('B', -1)]

for item in mix:
    wurf.seiteDrehen(item[0], item[1])

solve =[('Y', 1), ('G', 1), ('B', 1), ('B', 1), ('Y', 1), ('O', 1), ('Y', -1), ('B', -1), ('Y', 1), ('O', -1), ('Y', -1), ('B', 1), ('B', 1), ('Y', 1), ('Y', 1), ('R', 1), ('R', 1), ('Y', -1), ('Y', -1), ('Y', -1), ('O', 1), ('O', 1), ('Y', -1), ('R', 1), ('R', 1), ('Y', -1), ('Y', -1), ('B', 1), ('B', 1), ('Y', -1), ('G', 1), ('G', 1), ('Y', -1), ('Y', -1), ('G', 1), ('Y', 1), ('G', -1), ('Y', -1), ('B', 1), ('Y', 1), ('B', -1), ('Y', -1), ('B', 1), ('Y', 1), ('B', -1), ('Y', -1), ('B', 1), ('Y', 1), ('B', -1), ('Y', -1), ('Y', -1), ('Y', -1), ('Y', -1), ('R', -1), ('Y', -1), ('R', 1), ('Y', 1), ('G', 1), ('Y', 1), ('G', -1), ('Y', -1), ('Y', -1), ('Y', -1), ('Y', -1), ('Y', -1), ('O', -1), ('Y', -1), ('O', 1), ('Y', 1), ('B', 1), ('Y', 1), ('B', -1), ('Y', -1), ('Y', -1), ('Y', -1), ('Y', 1), ('R', 1), ('Y', 1), ('R', -1), ('Y', -1), ('B', -1), ('Y', -1), ('B', 1), ('Y', 1), ('Y', -1), ('Y', -1), ('Y', -1), ('Y', 1), ('O', 1), ('Y', 1), ('O', -1), ('Y', -1), ('G', -1), ('Y', -1), ('G', 1), ('Y', 1), ('R', 1), ('G', 1), ('Y', 1), ('G', -1), ('Y', -1), ('R', -1), ('R', 1), ('G', 1), ('Y', 1), ('G', -1), ('Y', -1), ('R', -1)]
for item in solve:
    wurf.seiteDrehen(item[0], item[1])
"""


farb = Farbchecker()
wurf = Wuerfel()
solve = CubeSolver(wurf)

print(wurf.colorPrint())

wurf.mischen(1000)
# print(wurf.cubeHistory)

print(wurf.colorPrint())

solve.solveCube()

print(wurf.colorPrint())
print(solve.getHistory())




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

