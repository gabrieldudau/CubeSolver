from Robot.Motors.AdvMotor import AdvMotor

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class DownTurnMotor(AdvMotor):
    
    def __init__(self, port) -> None:
        super().__init__(port)
        self.drehungWinkel = 90
        self.drehungGeschwindigkeit = 500
        
    def halbeDrehung(self, speed, anzahl):
        self.drehungGeschwindigkeit = speed
        self.drehungWinkel = 45
        self.drehung(anzahl)
        self.drehungWinkel = 90
        self.drehungGeschwindigkeit = 500

        