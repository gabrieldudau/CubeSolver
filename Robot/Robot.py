from Robot.Motors.DownTurnMotor import DownTurnMotor
from Robot.Motors.SidePushMotor import SidePushMotor
from Robot.Motors.SideTurnMotor import SideTurnMotor
from Robot.Sensors.AdvColorSensor import AdvColorSensor
from Robot.Cube.Cube import Wuerfel
from Robot.Cube.CubeSolver import CubeSolver
from pybricks.tools import wait

class Robot: 
    def __init__(self, portDownTurn:str, portSidePush:str, portSideTurn:str, portColSens:str) -> None:
        
        # Das sind alles tatsächliche, existierende Objekte, welche hier als Objekte modeliert werden.
        
        self.__downTurn = DownTurnMotor(portDownTurn)
        self.__sidePush = SidePushMotor(portSidePush)
        self.__sideTurn = SideTurnMotor(portSideTurn)
        self.__colSens = AdvColorSensor(portColSens)
        
        # Diese Klassen sind nur Digital. Sie modelieren und lösen den Würfel, sodass der Roboter mit seinen
        # Motoren und Sensoren den Würfel lösen kann. 
        
        self.cube = Wuerfel()
        self.cubeSolver = CubeSolver(self.cube)
        
    def getFarben(self):
        whiteCols = []
        for i in range(0,8):
            whiteCols.append(self.__colSens.scanCol())
            wait(500)
            self.__downTurn.halbeDrehung(400, 1)
        
    
    