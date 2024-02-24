from Cube import Wuerfel

class CubeSolver:
    """### Diese Klasse löst den Würfel
    Es ist notwendig, ein Objekt der Klasse Würfel zu bekommen. Anschließend wird mit den jeweiligen Methoden dieser Klasse, wie zum Beispiel
    makeKreuz() das eingegebene Würfel-Objekt "gelöst. Die dazu gebrauchten Bewegungen werden gespeichert. Man kann diese mit getHistory() bekommen.
    """
    def __init__(self, cube:Wuerfel):
        self.cube = cube
        self.__solvehistory = []
        self.__ecken = []
        self.__kanten = []
        
    
    def getHistory(self):
        return self.__solvehistory
    
    def makeKreuz(self):
        whiteSides = []
        
        # Die Liste middles erspart und später Code. Damit kann man gewisse Algorithmen verkürzen.
        
        middles = ["B", "R", "G", "O", "B", "R", "G", "O"]
        for i in range(1,13):
            if "W" in self.cube.getSide(i):
                whiteSides.append(i)
        print(whiteSides)
        
        middleWhite = list(set([5, 6, 7, 8]).intersection(set(whiteSides)))
        
        for p in middleWhite:
            self.cube.seiteDrehen(middles[p-5], 1)
            self.__solvehistory.append((middles[p-5], 1))
            self.cube.seiteDrehen("Y", 1)
            self.__solvehistory.append(("Y", 1))
            self.cube.seiteDrehen(middles[p-5], -1)
            self.__solvehistory.append((middles[p-5], -1))
            self.cube.seiteDrehen("Y", -1)
            self.__solvehistory.append(("Y", -1))
        
        whiteSides.clear()
        for i in range(1,13):
            if "W" in self.cube.getSide(i):
                whiteSides.append(i)
        
        print(whiteSides)
        
        downWhite = list(set([9, 10, 11, 12]).intersection(set(whiteSides)))
        
        for p in downWhite:
            if self.cube.getSide(p)[1] != "W":
                self.cube.seiteDrehen(middles[p-9], 1)
                self.__solvehistory.append((middles[p-9], 1))
                self.cube.seiteDrehen(middles[p-9], 1)
                self.__solvehistory.append((middles[p-9], 1))
        
        whiteSides.clear()
        for i in range(1,13):
            if "W" in self.cube.getSide(i):
                whiteSides.append(i)
        
        print(whiteSides)
        
        downWhite = list(set([9, 10, 11, 12]).intersection(set(whiteSides)))
        
        middleWhite = list(set([5, 6, 7, 8]).intersection(set(whiteSides)))
        
        upperWhite = list(set([1, 2, 3, 4]).intersection(set(whiteSides)))
            
        
        if len(upperWhite) > 0:
            while len(upperWhite) > 0:
                
                upper = upperWhite[0]
                if self.cube.getSide(upper)[0] != "W":
                    col = self.cube.getSide(upper)[0]
                    hMiddles = [middles[i] for i in range(upper-1 , upper + 3)]
                    for i in range(0, hMiddles.index(col)):
                        self.cube.seiteDrehen("Y", -1)
                        self.__solvehistory.append(("Y", -1))
                        
                    self.cube.seiteDrehen(col, 1)
                    self.__solvehistory.append((col, 1))
                    
                    self.cube.seiteDrehen(col, 1)
                    self.__solvehistory.append((col, 1))
                    
                    print("upper white solve")

                    
                else:
                    col = self.cube.getSide(upper)[1]
                    hMiddles = [middles[i] for i in range(upper-1 , upper + 3)]
                    for i in range(0, hMiddles.index(col)):
                        self.cube.seiteDrehen("Y", -1)
                        self.__solvehistory.append(("Y", -1))
                        
                    self.cube.seiteDrehen("Y", -1)
                    self.__solvehistory.append(("Y", -1))
                    
                    self.cube.seiteDrehen(middles[middles.index(col)+1], -1)
                    self.__solvehistory.append((middles[middles.index(col)+1], -1))
                    
                    self.cube.seiteDrehen(col, 1)
                    self.__solvehistory.append((col, 1))
                    
                    self.cube.seiteDrehen(middles[middles.index(col)+1], -1)
                    self.__solvehistory.append((middles[middles.index(col)+1], -1))
                    
                    print("upper color solve")
                    
                whiteSides.clear()
                
                for i in range(1,13):
                    if "W" in self.cube.getSide(i):
                        whiteSides.append(i)
                upperWhite = list(set([1, 2, 3, 4]).intersection(set(whiteSides)))
                middleWhite = list(set([5, 6, 7, 8]).intersection(set(whiteSides)))
                
                for p in middleWhite:
                    
                    self.cube.seiteDrehen(middles[p-5], 1)
                    self.__solvehistory.append((middles[p-5], 1))
                    
                    self.cube.seiteDrehen("Y", 1)
                    self.__solvehistory.append(("Y", 1))
                    
                    self.cube.seiteDrehen(middles[p-5], -1)
                    self.__solvehistory.append((middles[p-5], -1))
                    
                    self.cube.seiteDrehen("Y", -1)
                    self.__solvehistory.append(("Y", -1))
                    
                upperWhite = list(set([1, 2, 3, 4]).intersection(set(whiteSides)))
                middleWhite = list(set([5, 6, 7, 8]).intersection(set(whiteSides)))
                
                downWhite = list(set([9, 10, 11, 12]).intersection(set(whiteSides)))
        
                for p in downWhite:
                    if self.cube.getSide(p)[1] != "W":
                        
                        self.cube.seiteDrehen(middles[p-9], 1)
                        self.__solvehistory.append((middles[p-9], 1))
                        
                        self.cube.seiteDrehen(middles[p-9], 1)
                        self.__solvehistory.append((middles[p-9], 1))
                
                whiteSides.clear()
                for i in range(1,13):
                    if "W" in self.cube.getSide(i):
                        whiteSides.append(i)
                
                downWhite = list(set([9, 10, 11, 12]).intersection(set(whiteSides)))
                upperWhite = list(set([1, 2, 3, 4]).intersection(set(whiteSides)))
                middleWhite = list(set([5, 6, 7, 8]).intersection(set(whiteSides)))
    
    def solveCorner(self):
        self.makeKreuz()
        
        self.__curentEcken()
        
        
        
        
            
    def _eckeMicro1(self, col):
        """Ecke von oben nach unten bringen"""
        col = ["B", "R", "G", "O", "B"][["B", "R", "G", "O", "B"].index(col) + 1]
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen("Y", 1)
        self.__solvehistory.append(("Y", 1))
        
        self.cube.seiteDrehen(col, -1)
        self.__solvehistory.append((col, -1))
        
        self.cube.seiteDrehen("Y", -1)
        self.__solvehistory.append(("Y", -1))
        
        self.__curentEcken()
    
    
    def _eckeMicro2(self, col):
        col = ["B", "R", "G", "O", "B"][["B", "R", "G", "O", "B"].index(col) + 1]
        
        self.cube.seiteDrehen("Y", 1)
        self.__solvehistory.append(("Y", 1))
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen("Y", -1)
        self.__solvehistory.append(("Y", -1))
        
        self.cube.seiteDrehen(col, -1)
        self.__solvehistory.append((col, -1))
        
        self.__curentEcken()
        
    
    def __curentEcken(self):
        self.__ecken.clear()
        self.__ecken = self.cube.getCorners()