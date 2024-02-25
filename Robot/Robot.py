from Motors.DownTurnMotor import DownTurnMotor
from Motors.SidePushMotor import SidePushMotor
from Motors.SideTurnMotor import SideTurnMotor
from Sensors.AdvColorSensor import AdvColorSensor

class Robot: 
    def __init__(self, portDownTurn:str, portSidePush:str, portSideTurn:str, portColSens:str) -> None:
        
        # Das sind alles tatsächliche, existierende Objekte, welche hier als Objekte modeliert werden.
        
        self.__downTurn = DownTurnMotor(portDownTurn)
        self.__sidePush = SidePushMotor(portSidePush)
        self.__sideTurn = SideTurnMotor(portSideTurn)
        self.__colSens = AdvColorSensor(portColSens)
        
        # Diese Klassen sind nur Digital. Sie modelieren und lösen den Würfel, sodass der Roboter mit seinen
        # Motoren und Sensoren den Würfel lösen kann. 
        
        
        