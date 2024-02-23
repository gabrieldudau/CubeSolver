import copy
import random

ORANGE_BACKGROUND = '\033[48;2;255;165;0m'
RED_Background = '\033[48;2;255;0;0m'
GREEN_Background = '\033[48;2;0;255;0m'
BLUE_Background = '\033[48;2;0;0;255m'
WHITE_Background = '\033[48;2;255;255;255m'
YELLOW_Background = '\033[48;2;255;255;0m'
BLACK_Background = '\033[0;0;0;0;0m'

class Wuerfel:
    """
    ---
    ### DEN WÜRFEL RICHTIG EINLESEN:
    ----
    Die weiße Seite nach unten ausrichten, und die gelbe nach oben. Die blaue Seite steht zu einem selbst. 
    Von den restlichen Farben ist die Oberste die Nummer 1. Von gelb, ist die Seite die nach hinten zeigt die Nummer 1. 
    Weiß hat als Nummer 1 die Seite die quasi zu einem selbst zeigt. 
    -----
    """
    
    def __init__(self):
        self.cube = dict({})
        for color in ["R", "Y", "O", "W", "B", "G"]:
        
            self.cube[color] = [color,color,color,color,color,color,color,color]
        self.cubeHistory = []

    def getCorner(self, nummer:int) -> list:
        """Die Ecken werden von oben links vorne nach rechts durchnumeriert, und dann unten auch von links unten vorne durchnumeriert"""
        short = self.cube
                              # Die Ecke wird als Liste ausgegeben. Die erste Farbe zeigt zu einem selbst oder weg von einem, die zweite nach oben und die dritte seitlich
        if nummer == 1:  return[short["B"][8 - 1], short["Y"][6 - 1], short["O"][2 - 1]]
        elif nummer == 2: return[short["B"][2 - 1], short["Y"][4 - 1], short["R"][8 - 1]]
        elif nummer == 3: return[short["G"][8 - 1], short["Y"][2 - 1], short["R"][2 - 1]]
        elif nummer == 4: return[short["G"][2 - 1], short["Y"][8 - 1], short["O"][8 - 1]]
        elif nummer == 5: return[short["B"][6 - 1], short["W"][8 - 1], short["O"][4 - 1]]
        elif nummer == 6: return[short["B"][4 - 1], short["W"][2 - 1], short["R"][6 - 1]]
        elif nummer == 7: return[short["G"][6 - 1], short["W"][4 - 1], short["R"][4 - 1]]
        elif nummer == 8: return[short["G"][4 - 1], short["W"][6 - 1], short["O"][6 - 1]]
        else: return[None, None, None]

    def getCorners(self):
        return [self.getCorner(i)for i in range (1, 9)]
    
    def getSide(self, nummer):
        """ - Oben ist die Seite die zu einem zeigt Nr. 1, die rechts davon 2 usw.
                - Die erste Farbe zeigt zur Seite, die zweite nach oben.
            - Unten genau so. 
                - Die erste Farbe zur Seite, die zweite nach unten.
            - Für die mittlere Schicht fängt man mit der Kante links von blau (Nr. 5), und geht nach rechts.
                - Farbe Nr. 1 zeigt zu einem selbst, oder weg von einem, Nr. 2 zeigt zur Seite.
        """
        short = self.cube
        if nummer ==  1 : return[short["B"][0], short["Y"][4]]
        elif nummer ==  2 : return[short["R"][0], short["Y"][2]]
        elif nummer ==  3 : return[short["G"][0], short["Y"][0]]
        elif nummer ==  4 : return[short["O"][0], short["Y"][6]]
        elif nummer ==  5 : return[short["B"][6], short["O"][2]]
        elif nummer ==  6 : return[short["B"][2], short["R"][6]]
        elif nummer ==  7 : return[short["G"][6], short["R"][2]]
        elif nummer ==  8 : return[short["G"][2], short["O"][6]]
        elif nummer ==  9 : return[short["B"][4], short["W"][0]]
        elif nummer ==  10: return[short["R"][4], short["W"][2]]
        elif nummer ==  11: return[short["G"][4], short["W"][4]]
        elif nummer ==  12: return[short["O"][4], short["W"][6]]
        else: return[]
            
    

    def seiteDrehen(self, farbe:str, richtung:int):                            # Richtung entweder 1 (-> Uhrzeiger) oder -1 (-> gegen Uhrzeiger)
        if farbe not in self.cube.keys() and richtung > 1 and richtung < 1 :
            return
            
        if farbe ==  "B":
            copycube = copy.deepcopy(self.cube)
            if richtung == 1:
                self.cube["Y"][3:6] = copycube["O"][1:4]
                self.cube["R"][5:8] = copycube["Y"][3:6]
                self.cube["W"][7], self.cube["W"][0], self.cube["W"][1] = copycube["R"][5], copycube["R"][6], copycube["R"][7]
                self.cube["O"][1:4] = copycube["W"][7], copycube["W"][0], copycube["W"][1]
                self.cube["B"] = [self.cube["B"][i - 2]for i in range(8)]
                self.cubeHistory.append(("B",1))
            if richtung == -1:
                self.cube["Y"][3:6] = copycube["R"][5:8]
                self.cube["R"][5:8] = [copycube["W"][7], copycube["W"][0], copycube["W"][1]]
                self.cube["W"][7], self.cube["W"][0], self.cube["W"][1] = self.cube["O"][1:4]
                self.cube["O"][1:4] = copycube["Y"][3:6]
                self.cube["B"] = [self.cube["B"][i]for i in range(2,8)] + self.cube["B"][0:2]
                self.cubeHistory.append(("B",-1))
        
        if farbe ==  "Y":
            copycube = copy.deepcopy(self.cube)
            if richtung == 1:
                self.cube["B"][7], self.cube["B"][0], self.cube["B"][1] = copycube["R"][7], copycube["R"][0], copycube["R"][1]
                self.cube["R"][7], self.cube["R"][0], self.cube["R"][1] = copycube["G"][7], copycube["G"][0], copycube["G"][1]
                self.cube["G"][7], self.cube["G"][0], self.cube["G"][1] = copycube["O"][7], copycube["O"][0], copycube["O"][1]
                self.cube["O"][7], self.cube["O"][0], self.cube["O"][1] = copycube["B"][7], copycube["B"][0], copycube["B"][1]
                self.cube["Y"] = [self.cube["Y"][i - 2]for i in range(8)]
                self.cubeHistory.append(("Y",1))
            if richtung == -1:
                self.cube["B"][7], self.cube["B"][0], self.cube["B"][1] = copycube["O"][7], copycube["O"][0], copycube["O"][1]
                self.cube["R"][7], self.cube["R"][0], self.cube["R"][1] = copycube["B"][7], copycube["B"][0], copycube["B"][1]
                self.cube["G"][7], self.cube["G"][0], self.cube["G"][1] = copycube["R"][7], copycube["R"][0], copycube["R"][1]
                self.cube["O"][7], self.cube["O"][0], self.cube["O"][1] = copycube["G"][7], copycube["G"][0], copycube["G"][1]
                self.cube["Y"] = [self.cube["Y"][i]for i in range(2,8)] + self.cube["Y"][0:2]
                self.cubeHistory.append(("Y",-1))
        
        if farbe ==  "W":
            copycube = copy.deepcopy(self.cube)
            if richtung == 1:
                self.cube["B"][3:6] = copycube["O"][3:6]
                self.cube["R"][3:6] = copycube["B"][3:6]
                self.cube["G"][3:6] = copycube["R"][3:6]
                self.cube["O"][3:6] = copycube["G"][3:6]
                self.cube["W"] = [self.cube["W"][i - 2]for i in range(8)]
                self.cubeHistory.append(("W",1))
            if richtung == -1:
                self.cube["B"][3:6] = copycube["R"][3:6]
                self.cube["R"][3:6] = copycube["G"][3:6]
                self.cube["G"][3:6] = copycube["O"][3:6]
                self.cube["O"][3:6] = copycube["B"][3:6]
                self.cube["W"] = [self.cube["W"][i]for i in range(2,8)] + self.cube["W"][0:2]
                self.cubeHistory.append(("W",-1))
                
        if farbe ==  "R":
            copycube = copy.deepcopy(self.cube)
            if richtung == 1:
                self.cube["Y"][1:4] = copycube["B"][1:4]
                self.cube["G"][5:8] = copycube["Y"][1:4]
                self.cube["W"][1:4] = copycube["G"][5:8]
                self.cube["B"][1:4] = copycube["W"][1:4] 
                self.cube["R"] = [self.cube["R"][i - 2]for i in range(8)]
                self.cubeHistory.append(("R",1))
            if richtung == -1:
                self.cube["Y"][1:4] = copycube["G"][5:8]
                self.cube["G"][5:8] = copycube["W"][1:4] 
                self.cube["W"][1:4] = copycube["B"][1:4]
                self.cube["B"][1:4] = copycube["Y"][1:4]
                self.cube["R"] = [self.cube["R"][i]for i in range(2,8)] + self.cube["R"][0:2]
                self.cubeHistory.append(("R",-1))
        
        if farbe ==  "O":
            copycube = copy.deepcopy(self.cube)
            if richtung == 1:
                self.cube["Y"][5:8] = copycube["G"][1:4]
                self.cube["B"][5:8] = copycube["Y"][5:8]
                self.cube["W"][5:8] = copycube["B"][5:8]
                self.cube["G"][1:4] = copycube["W"][5:8] 
                self.cube["O"] = [self.cube["O"][i - 2]for i in range(8)]
                self.cubeHistory.append(("O",1))
            if richtung == -1:
                self.cube["Y"][5:8] = copycube["B"][5:8]
                self.cube["B"][5:8] = copycube["W"][5:8]
                self.cube["W"][5:8] = copycube["G"][1:4]
                self.cube["G"][1:4] = copycube["Y"][5:8]
                self.cube["O"] = [self.cube["O"][i]for i in range(2,8)] + self.cube["O"][0:2]
                self.cubeHistory.append(("O",-1))
                
        if farbe ==  "G":
            copycube = copy.deepcopy(self.cube)
            if richtung == 1:
                self.cube["O"][5:8] = [copycube["Y"][7], copycube["Y"][0], copycube["Y"][1]]
                self.cube["R"][1:4] = copycube["W"][3:6]
                self.cube["Y"][7], self.cube["Y"][0], self.cube["Y"][1] = copycube["R"][1], copycube["R"][2], copycube["R"][3]
                self.cube["W"][3:6] = copycube["O"][5:8]
                self.cube["G"] = [self.cube["G"][i - 2]for i in range(8)]
                self.cubeHistory.append(("G",1))
            if richtung == -1:
                self.cube["O"][5:8] = copycube["W"][3:6]
                self.cube["R"][1:4] = [copycube["Y"][7], copycube["Y"][0], copycube["Y"][1]]
                self.cube["Y"][7], self.cube["Y"][0], self.cube["Y"][1] = copycube["O"][5:8]
                self.cube["W"][3:6] = copycube["R"][1:4]
                self.cube["G"] = [self.cube["G"][i]for i in range(2,8)] + self.cube["G"][0:2]
                self.cubeHistory.append(("G",-1))
                
                    
    def setFarbenFuerSeite(self, seite:str, position:int, farbe:str):           # Zählen von 1 zu 9
        if seite in self.cube.keys() and position > 0 and position < 9 and farbe in self.cube.keys():
            self.cube[seite][position-1] = farbe
        else:
            print("error - wrong input")
        
    def mischen(self, zuege:int):
        for i in range (zuege):
            seite = random.randint(0,5)
            self.seiteDrehen(list(self.cube.keys())[seite], random.choice([-1,1]) )

    def __ausgabeSeite(self, color) -> str:
        if color in self.cube.keys():
            out = ""
            out += str(color) + " ---> | "
            for item in range(0, len(self.cube[color])):
                col = str(self.cube[color][item])
                if len(col) != 4:
                    col = " "+str(col)+"  "
                out += str(item)+ " - " + col + " | "
            out += "\n"
            return out
        else:
            return "wrong input -> color not existent"
        
    
    def printAlt(self) -> str:
        out = ""
        for key in self.cube.keys():
            out += str(self.__ausgabeSeite(key))
        return out

    def __str__(self) -> str:
        return self.colorPrint() + "\n\n"
            




