from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class AdvMotor:
    
    def __init__(self, port ) -> None:
        self.motor = Motor(port)
        self.drehungWinkel = 90
        self.drehungGeschwindigkeit = 500

    
    def normaleDrehung(self, anzahl, direction):
        self.motor.run_angle(direction * self.drehungGeschwindigkeit, anzahl*self.drehungWinkel)
    
    