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
        self.__curentEcken()
        
        self.__kanten = []
        self.__curentKanten()
        
        self.__whiteKanten = []     # Die Position der weißen Kanten als Zahl
        
        
    
    def getHistory(self):
        return self.__solvehistory
    
    
    
    def makeKreuz(self):
        self.__curentTeile()
        
        # Hier werden die oberen Kanten gelöst. Wenn eine Kante mit weiß nach oben zeigt passt es, ansonsten
        # dreht man sie, sodass die weiße Seite der Kante nach oben zeigt. Es gibt nur einen Fall.    
        
        upperWhite = list(set(self.__whiteKanten).intersection([1,2,3,4]))
        notwendige = [self.__kanten[i][0] for i in range(0,4)]
    
        while True:
            if not "W" in notwendige:
                break
            else:
                self.kanteMicroUp(notwendige.index("W") + 1)
            notwendige = [self.__kanten[i][0] for i in range(0,4)]
        
        # Hier lösen wir die Mitten. Hierbei kommt es manchmal dazu, dass eine weiße Kante die in der 
        # Mitte steht in die untere Schicht getan wird, das ist aber nicht schlimm, denn es wird als 
        # nächstes dann wieder hochgeholt. Man unterscheidet zwischen zwei Fällen, deswegen zwei Micros.
        
        middleWhite = list(set(self.__whiteKanten).intersection([5,6,7,8]))
        
        while len(middleWhite) > 0:
            if middleWhite[0] in [5,7]:
                if self.__kanten[middleWhite[0]-1][0] == "W":
                    self.kanteMicroMid1(middleWhite[0])
                else: 
                    self.kanteMicroMid2(middleWhite[0])
            else:
                if self.__kanten[middleWhite[0]-1][0] == "W":
                    self.kanteMicroMid2(middleWhite[0])
                else: 
                    self.kanteMicroMid1(middleWhite[0])
            middleWhite = list(set(self.__whiteKanten).intersection([5,6,7,8]))
        
        # Hier werden die unteren weißen Kanten behandelt. Es gibt wieder zwei Fälle, eine weiße Seite der Kante 
        # zeigt nach unten, oder eben nicht. 
        
        lowWhite = list(set(self.__whiteKanten).intersection([9,10,11,12]))
        
        for kante in lowWhite:
            if self.__kanten[kante-1][1] == "W":
                self.kanteMicroLow1(kante)
            else:
                self.kanteMicroLow2(kante)
        
        # Nun sind alle Kanten die eine weiße Seite haben nach oben ausgerichtet. Jetzt werden diese weißen Seiten
        # zurechtgerückt und einfach nach oben geschoben. Das weiße Kreuz wird dadurch gebildet. Wir brauchen 
        # hier nur eine Methode. 
        
        self.kanteMicroFix()

    def kanteMicroUp(self, num:int):
        """benutzt falls Kante oben ist, aber weiß nicht nach oben sondern seitlich zeigt"""
        middles = ["B","R","G","O"]
        col = middles[num-1]
        
        self.cube.seiteDrehen(col, -1)
        self.__solvehistory.append((col, -1))
        
        self.cube.seiteDrehen(middles[num - 2], -1)
        self.__solvehistory.append((middles[num - 2], -1))
        
        self.cube.seiteDrehen("Y", -1)
        self.__solvehistory.append(("Y", -1))
        
        self.cube.seiteDrehen(middles[num - 2], 1)
        self.__solvehistory.append((middles[num - 2], 1))
        
        self.__curentTeile()

    def kanteMicroMid1(self, num:int):
        """benutzt bei besonderem Fall der mittleren Kanten"""
        middles = ["B","R","G","O"]
        col = middles[num-6]
        
        if num == 5:
            zugehoerigeKante = 4
        else: 
            zugehoerigeKante = num - 5
        
        while "W" in self.__kanten[zugehoerigeKante - 1]:
            self.cube.seiteDrehen("Y", 1)
            self.__solvehistory.append(("Y", 1))
            self.__curentTeile()
        
        self.cube.seiteDrehen(col, -1)
        self.__solvehistory.append((col, -1))
        
        self.__curentTeile()

    def kanteMicroMid2(self, num:int):
        """benutzt bei besonderem Fall der mittleren Kanten"""
        middles = ["B","R","G","O"]
        col = middles[num-5]
        
        zugehoerigeKante = num - 4
        
        while "W" in self.__kanten[zugehoerigeKante - 1]:
            self.cube.seiteDrehen("Y", 1)
            self.__solvehistory.append(("Y", 1))
            self.__curentTeile()
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.__curentTeile()

    def kanteMicroLow1(self, num:int):
        """benutzt wenn untere Kante mit weiß nach unten zeigt und lediglich gedreht werden muss"""
        
        middles = ["B","R","G","O"]
        col = middles[num - 9]
        zugehoerigeKante = num - 8
        
        while "W" in self.__kanten[zugehoerigeKante - 1]:
            self.cube.seiteDrehen("Y", 1)
            self.__solvehistory.append(("Y", 1))
            self.__curentTeile()
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.__curentTeile()

    def kanteMicroLow2(self, num:int):
        """benutzt wenn untere Kante mit weiß seitlich zeigt und mehr angepasst werden muss"""
        middles = ["B","R","G","O"]
        col = middles[num - 9]
        zugehoerigeKante = num - 8
        
        while "W" in self.__kanten[zugehoerigeKante - 1]:
            self.cube.seiteDrehen("Y", 1)
            self.__solvehistory.append(("Y", 1))
            self.__curentTeile()
        
        # Ich saß so lange hier dran... 
        # Ich hab diesen Algorithmus jetzt selbst erstellt, weiß nicht ob es effektiver geht.
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen("Y", 1)
        self.__solvehistory.append(("Y", 1))
        
        self.cube.seiteDrehen(middles[num - 10], 1)
        self.__solvehistory.append((middles[num - 10],1))
        
        self.cube.seiteDrehen("Y", -1)
        self.__solvehistory.append(("Y", -1))
        
        self.cube.seiteDrehen(col, -1)
        self.__solvehistory.append((col, -1))
        
        self.cube.seiteDrehen("Y", 1)
        self.__solvehistory.append(("Y", 1))
        
        self.cube.seiteDrehen(middles[num - 10], -1)
        self.__solvehistory.append((middles[num - 10],-1))
        
        self.cube.seiteDrehen("Y", -1)
        self.__solvehistory.append(("Y", -1))
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        # Es geht glaube ich nicht mit weniger moves, weil man muss es halt so bewegen, sodass 
        # keine anderen zerstört werden. 
        
        self.__curentTeile()

    def kanteMicroFix(self):
        """wenn alle Kanten mit weiß oben stehen und mit weiß nach oben zeigen dann bringt diese Methode sie in die Richtige Position"""
        middles = ["B","R","G","O"]
        for i in range(0,4):
            for j in range(0,4):
                if self.__kanten[j][1] == "W":
                    colorIndex = j
                    break
            
            while self.__kanten[colorIndex%4][0] != middles[colorIndex%4]:
                self.cube.seiteDrehen("Y", -1)
                self.__solvehistory.append(("Y", -1))
                
                colorIndex += 1
                
                self.__curentTeile()
            
            self.cube.seiteDrehen(middles[colorIndex%4], 1)
            self.__solvehistory.append((middles[colorIndex%4], 1))
            
            self.cube.seiteDrehen(middles[colorIndex%4], 1)
            self.__solvehistory.append((middles[colorIndex%4], 1))
            
            self.__curentTeile()
    
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
        
    
    def __curentKanten(self):
        self.__kanten.clear()
        self.__kanten = [self.cube.getSide(i) for i in range (1,13)]
    
    def __curentEcken(self):
        self.__ecken.clear()
        self.__ecken = self.cube.getCorners()
    
    def __curentTeile(self):
        self.__curentEcken()
        self.__curentKanten()
        
        self.__whiteKanten.clear()
        for i in range(0,12):
            if "W" in self.__kanten[i]:
                self.__whiteKanten.append(i+1)
    
        