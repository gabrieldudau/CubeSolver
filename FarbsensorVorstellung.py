from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from Robot.Sensors.Farbchecker import Farbchecker
from Robot.Sensors.AdvColorSensor import AdvColorSensor
from pybricks.parameters import Port


colSens = AdvColorSensor(Port.S1)
ev3 = EV3Brick()

while True:
    colors = colSens.farbSensor.rgb()
    

    if Button.DOWN in ev3.buttons.pressed():

        ev3.screen.clear()

        print("R:" + str(colors[0]) + "-G:" + str(colors[1])+ "-B:" + str(colors[2]))

        out = "R:" + str(colors[0]) + "-G:" + str(colors[1])+ "-B:" + str(colors[2])

        ev3.screen.print(out)

        ev3.screen.print(str(colSens.scanCol(colors[0], colors[1], colors[2])))

        print(str(colSens.farbChecker.rubColWArea(colors[0], colors[1], colors[2])))


    if Button.UP in ev3.buttons.pressed() :
        break
    
