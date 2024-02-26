from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from Farbchecker import Farbchecker


class AdvColorSensor:
    def __init__(self, port:str) -> None:
        self.farbSensor = ColorSensor(port)
        self.farbChecker = Farbchecker()
    
    def scanCol(self) -> str :
        colors = self.farbSensor.rgb()
        col = self.farbChecker.rubColWArea(colors)
    