from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from Robot.Sensors.Farbchecker import Farbchecker


class AdvColorSensor:
    def __init__(self, port:Port) -> None:
        self.farbSensor = ColorSensor(port)
        self.farbChecker = Farbchecker()
    
    def scanCol(self) -> str :
        colors = self.farbSensor.rgb()
        col = self.farbChecker.rubColWArea(colors[0], colors[1], colors[2])
        return col
    