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


farb = Farbchecker()


colSens = ColorSensor(Port.S1)

downTurn = DownTurnMotor(Port.A)


drehhMot = SidePushMotor(Port.B)

pushMot = SidePushMotor(Port.C)

"""
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
    
rob = Robot(ev3, Port.A, Port.B, Port.C, Port.S1)

Farbspeicher = []

"alle Farben, die zu Beginn oben sind werden eingescant"

downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())
wait(3000)
downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())
wait(1000)
downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())
wait(1000)
downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())
wait(1000)
downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())
wait(1000)
downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())
wait(1000)
downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())
wait(1000)
downTurn.halbesDrehung(1,1)
Farbspeicher.append(colSens.rgb())

print(Farbspeicher)

"schwarze Werte: [(2, 3, 7), (2, 3, 6), (2, 3, 5), (2, 3, 7), (2, 3, 6), (3, 3, 8), (2, 3, 6)]"
"rote Werte: [(18, 8, 15), (24, 9, 20), (20, 8, 15), (26, 9, 22), (19, 8, 16), (24, 10, 21), (19, 8, 15)]"
"grüne Werte: [(7, 21, 61), (9, 23, 86), (8, 21, 63), (10, 24, 90), (8, 21, 66), (9, 24, 89), (8, 21, 67)]"
"weiße Werte: [(24, 29, 64), (31, 35, 94), (23, 29, 61), (30, 34, 88), (25, 29, 62), (29, 33, 83), (26, 31, 68)]"
"blaue Werte: [(5, 20, 48), (6, 23, 70), (5, 20, 52), (6, 23, 72), (6, 21, 59), (6, 23, 74), (6, 22, 59)]"
"orangene Werte: [(17, 26, 72), (26, 34, 100), (21, 29, 89), (26, 33, 100), (21, 30, 100), (27, 34, 100), (23, 31, 100)]"




"""
drehhMot.motor.run_until_stalled(100)
drehhMot.motor.run_until_stalled(10)
wait(200)
pushMot.motor.run_until_stalled(100)
drehhMot.motor.run_angle(-200, 105)
pushMot.motor.run_until_stalled(-100)
"""