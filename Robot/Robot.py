import copy
from Robot.Motors.DownTurnMotor import DownTurnMotor
from Robot.Motors.SidePushMotor import SidePushMotor
from Robot.Motors.SideTurnMotor import SideTurnMotor
from Robot.Sensors.AdvColorSensor import AdvColorSensor
from Robot.Cube.Cube import Wuerfel
from Robot.Cube.CubeSolver import CubeSolver
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port

class Robot: 
    def __init__(self,ev3:EV3Brick, portDownTurn:Port, portSidePush:Port, portSideTurn:Port, portColSens:Port) -> None:
        
        # Das sind alles tatsächliche, existierende Objekte, welche hier als Objekte modeliert werden.
        
        self.ev3 = ev3
        self.__downTurn = DownTurnMotor(portDownTurn)
        self.__sidePush = SidePushMotor(portSidePush)
        self.__sideTurn = SideTurnMotor(portSideTurn)
        self.__colSens = AdvColorSensor(portColSens)
        
        # Diese Klassen sind nur Digital. Sie modelieren und lösen den Würfel, sodass der Roboter mit seinen
        # Motoren und Sensoren den Würfel lösen kann. 
        
        self.cube = Wuerfel()
        self.cubeSolver = CubeSolver(self.cube)
        
        
        self.curentColor = "R"
        
    def getFarben(self):
        whiteCols = {}
        redCols = {}
        greenCols = {}
        orangeCols  ={}
        blueCols = {}
        yellowCols = {}
        
        
        for i in range(1,9):
            whiteCols[i] = self.__colSens.scanCol()
            self.ev3.screen.print(str(i) + " - >" + str(whiteCols[i]))
            print(whiteCols[i])
            wait(500)
            self.__downTurn.halbeDrehung(100,1)
            wait(500)
        
        self.__downTurn.halbeDrehung(400, 1)
        
        
        
        
        
        for index in whiteCols:
            self.cube.setFarbenFuerSeite("W", index, whiteCols[index])
            
        for index in redCols:
            self.cube.setFarbenFuerSeite("R", index, redCols[index])

        for index in greenCols:
            self.cube.setFarbenFuerSeite("G", index, greenCols[index])

        for index in orangeCols:
            self.cube.setFarbenFuerSeite("O", index, orangeCols[index])

        for index in blueCols:
            self.cube.setFarbenFuerSeite("B", index, blueCols[index])

        for index in yellowCols:
            self.cube.setFarbenFuerSeite("Y", index, yellowCols[index])
        
        print(self.cube)
        
        print("Do you want to correct something? (y-Yes | n-No)")
        eingabe = ""
        
        while eingabe != "y" and eingabe != "n":
            eingabe = input()
        
        
        
        if eingabe == "y":
            print("You have entered the edit menu. Write -q to leave. If not, you can correct a certain color "+
                  "by writing:\n-> SIDECOL - NUMBER - NEWCOL <-\nAn example would be:\n"+
                  "-> G - 1 - B <- \n")
            
            eingabe = input()
            while eingabe != "-q":
                try:
                    self.cube.setFarbenFuerSeite(list(eingabe)[0], int(list(eingabe)[4]), list(eingabe)[8])
                except:
                    print("wrong input")
                print("aktueller Wuerfel: \n" + str(self.cube))
                eingabe = input()

    def solveCube(self):
        self.cubeSolver.solveCube()
        
        history = copy.deepcopy(self.cubeSolver.getHistory())
        
        for elem in history:
            if elem[0] == "Y":
                self.gelbDrehen(elem[1])
            else:
                self.seiteDrehen(elem[0], elem[1])

    def wuerfelDrehen(self, col):
        middles = ["R","G","O","B"]
        
        while self.curentColor != col:
            print(self.curentColor)
            self.__downTurn.normaleDrehung(1, 1)
            self.curentColor = middles[(middles.index(self.curentColor) + 1)%4]
            print(self.curentColor)
            
    def seiteDrehen(self, col, direction): 
        """Kann alles drehen bis auf gelb, also "Y" """
        direction = direction * -1
        
        self.wuerfelDrehen(col)
        
        self.__sideTurn.motor.run_until_stalled(direction * 100)
        wait(100)
        self.__sideTurn.motor.run_until_stalled(direction * 10)
        
        self.__sidePush.pushTo_FromCube(100)
        
        wait(50)
        
        self.__sideTurn.motor.run_angle(200 * direction * -1, 108)
        
        self.__sidePush.pushTo_FromCube(-100)
        
        self.__sideTurn.motor.run_until_stalled(300)
        self.__sideTurn.motor.run_until_stalled(20)
        
        wait(100)
        self.__sideTurn.motor.run_angle(-50, 70)

    def gelbDrehen(self, direction):
        
        direction = direction * -1
        
        self.__sidePush.pushTo_FromCube(1500)
        wait(100)
        self.__sidePush.pushTo_FromCube(50)
        
        if direction == -1:
            self.__downTurn.normaleDrehung(1, 1)
        else:
            self.__downTurn.normaleDrehung(1, 1)
            self.__downTurn.normaleDrehung(1, 1)
            self.__downTurn.normaleDrehung(1, 1)
            
        self.__sidePush.pushTo_FromCube(-100)
        self.__sidePush.pushTo_FromCube(1500)
        self.__sidePush.pushTo_FromCube(-200)
        
        self.seiteDrehen(self.curentColor, -1)
        self.seiteDrehen(self.curentColor, 1)
        
        
        
        self.__sidePush.pushTo_FromCube(-100)
        
        
        