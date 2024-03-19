from Robot.Motors.AdvMotor import AdvMotor

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class SideTurnMotor(AdvMotor):
    
    def __init__(self, port):
        super().__init__(port)
        
        self.drehungWinkel = 105
        self.drehungGeschwindigkeit = -400     

    