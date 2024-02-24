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
print(wurf.colorPrint())


ev3 = EV3Brick()
colSens = ColorSensor(Port.S1)



    