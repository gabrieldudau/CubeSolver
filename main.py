#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from Cube import Wuerfel
from CubeSolver import CubeSolver
from Farbchecker import Farbchecker

# -----------------------------------------------------------------Testprogramm für PC ohne ev3-----------------------------------------------------------------


farb = Farbchecker()

wurf = Wuerfel()
solve = CubeSolver(wurf)

print(wurf.colorPrint())

# Dieser moveset hat Mal für Bugs gesorgt. Mit diesen Zeilen kann man gut testen. 

# 

# moveset = [('O', 1), ('B', 1), ('Y', 1), ('O', 1), ('W', 1), ('R', 1), ('W', 1), ('B', 1), ('B', 1), ('W', -1)]
# for item in moveset:
#     wurf.seiteDrehen(item[0], item[1])

wurf.mischen(10)
print(wurf.cubeHistory)

print(wurf.colorPrint())
solve.solveMidSides()

print(solve.getHistory())




    