from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Farbchecker import Farbchecker


# -----------------------------------------------------------------Testprogramm für ev3-----------------------------------------------------------------


farb = Farbchecker()

ev3 = EV3Brick()
colSens = ColorSensor(Port.S1)


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
    
    
    