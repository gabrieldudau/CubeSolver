#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Robot.Sensors.Farbchecker import Farbchecker
from Robot.Motors.DownTurnMotor import DownTurnMotor
from Robot.Motors.SidePushMotor import SidePushMotor
from Robot.Robot import Robot

# -----------------------------------------------------------------Testprogramm für ev3-----------------------------------------------------------------

"""
farb = Farbchecker()


colSens = ColorSensor(Port.S1)

downTurn = DownTurnMotor(Port.A)


drehhMot = SidePushMotor(Port.B)

pushMot = SidePushMotor(Port.C)

downTurn.drehung(4)

for i in range(6):
    drehhMot.motor.run_until_stalled(100)
    wait(100)
    drehhMot.motor.run_until_stalled(10)

    pushMot.motor.run_until_stalled(100)

    wait(400)
    drehhMot.motor.run_angle(-200, 105)

    pushMot.motor.run_until_stalled(-100)

    drehhMot.motor.run_until_stalled(50)
    wait(100)
    drehhMot.motor.run_angle(-50, 60)
"""

"""
while True:
    colors = colSens.rgb()
    

    if Button.DOWN in ev3.buttons.pressed():
        ev3.screen.clear()
        print(colors)
        out = "R:" + str(colors[0]) + "-G:" + str(colors[1])+ "-B:" + str(colors[2])
        ev3.screen.print(out)
        ev3.screen.print(str(farb.rubColWDif(colors[0], colors[1], colors[2])))
        print(str(farb.rubColWDif(colors[0], colors[1], colors[2])))
    if Button.UP in ev3.buttons.pressed() :
        break
"""
ev3 = EV3Brick()
    
rob = Robot(ev3, Port.A, Port.C, Port.B, Port.S1)

rob.getFarben()
