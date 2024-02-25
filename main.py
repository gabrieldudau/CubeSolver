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


farb = Farbchecker()

wurf = Wuerfel()
solve = CubeSolver(wurf)

print(wurf.colorPrint())

# Dieser moveset hat Mal für Bugs gesorgt. Mit diesen Zeilen kann man gut testen. 

"""
moveset = [('Y', -1), ('Y', 1), ('O', 1), ('B', -1), ('B', -1), ('G', -1), ('G', -1), ('R', 1), ('G', 1), ('O', 1)]
for item in moveset:
    wurf.seiteDrehen(item[0], item[1])
"""

wurf.mischen(1000)
print(wurf.cubeHistory)

print(wurf.colorPrint())
solve.solveUpperCross()

print(wurf.colorPrint())

print(solve.getHistory())




    