from Cube import Wuerfel

class CubeSolver:
    """### Diese Klasse löst den Würfel
    Es ist notwendig, ein Objekt der Klasse Würfel zu bekommen. Anschließend wird mit den jeweiligen Methoden dieser Klasse, wie zum Beispiel
    solveCross() das eingegebene Würfel-Objekt "gelöst. Die dazu gebrauchten Bewegungen werden gespeichert. Man kann diese mit getHistory() bekommen.
    """
    def __init__(self, cube:Wuerfel):
        self.cube = cube
        self.__solvehistory = []
        
        self.__ecken = []
        
        self.__kanten = []
        
        self.__whiteKanten = []     # Die Position der weißen Kanten als Zahl
        self.__whiteEcken = []      # Die Position der weißen Ecken als Zahl
        
        self.__curentTeile()
        
        
    
    def getHistory(self):
        return self.__solvehistory
    
    
    # ---------------------------------------------------------Anfang weißes Kreuz---------------------------------------------------------

    def solveCross(self):
        self.__curentTeile()
        
        # Hier werden die oberen Kanten gelöst. Wenn eine Kante mit weiß nach oben zeigt passt es, ansonsten
        # dreht man sie, sodass die weiße Seite der Kante nach oben zeigt. Es gibt nur einen Fall.    
        
        upperWhite = list(set(self.__whiteKanten).intersection([1,2,3,4]))
        notwendige = [self.__kanten[i][0] for i in range(0,4)]
    
        while True:
            if not "W" in notwendige:
                break
            else:
                self.__SCkanteMicroUp(notwendige.index("W") + 1)
            notwendige = [self.__kanten[i][0] for i in range(0,4)]
        
        # Hier lösen wir die Mitten. Hierbei kommt es manchmal dazu, dass eine weiße Kante die in der 
        # Mitte steht in die untere Schicht getan wird, das ist aber nicht schlimm, denn es wird als 
        # nächstes dann wieder hochgeholt. Man unterscheidet zwischen zwei Fällen, deswegen zwei Micros.
        
        middleWhite = list(set(self.__whiteKanten).intersection([5,6,7,8]))
        
        while len(middleWhite) > 0:
            if middleWhite[0] in [5,7]:
                if self.__kanten[middleWhite[0]-1][0] == "W":
                    self.__SCkanteMicroMid1(middleWhite[0])
                else: 
                    self.__SCkanteMicroMid2(middleWhite[0])
            else:
                if self.__kanten[middleWhite[0]-1][0] == "W":
                    self.__SCkanteMicroMid2(middleWhite[0])
                else: 
                    self.__SCkanteMicroMid1(middleWhite[0])
            middleWhite = list(set(self.__whiteKanten).intersection([5,6,7,8]))
        
        # Hier werden die unteren weißen Kanten behandelt. Es gibt wieder zwei Fälle, eine weiße Seite der Kante 
        # zeigt nach unten, oder eben nicht. 
        
        lowWhite = list(set(self.__whiteKanten).intersection([9,10,11,12]))
        
        for kante in lowWhite:
            if self.__kanten[kante-1][1] == "W":
                self.__SCkanteMicroLow1(kante)
            else:
                self.__SCkanteMicroLow2(kante)
        
        # Nun sind alle Kanten die eine weiße Seite haben nach oben ausgerichtet. Jetzt werden diese weißen Seiten
        # zurechtgerückt und einfach nach oben geschoben. Das weiße Kreuz wird dadurch gebildet. Wir brauchen 
        # hier nur eine Methode. 
        
        self.__SCkanteMicroFix()

    def __SCkanteMicroUp(self, num:int):
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

    def __SCkanteMicroMid1(self, num:int):
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

    def __SCkanteMicroMid2(self, num:int):
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

    def __SCkanteMicroLow1(self, num:int):
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

    def __SCkanteMicroLow2(self, num:int):
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

    def __SCkanteMicroFix(self):
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

# ----------------------------------------------------------Ende weißes Kreuz----------------------------------------------------------


# ---------------------------------------------------------Anfang untere Ecken---------------------------------------------------------

    def solveDownCorner(self):
        """Bei dieser Methode ist das weiße Kreuz gemacht. Der nächste Schritt sind also die Ecken. 
        Diese Methode erstellt zunächst ein weißes Kreuz und fängt dann an die Ecken zu lösen."""
        
        self.solveCross()
        
        print("________________________________________KREUZ__________________________________\n")
        print(self.cube.colorPrint())
        print("________________________________________________________________________________")
        
        self.__curentTeile()
        
        # Es wird unterschieden zwischen den oberen und den unteren Ecken. Down Ecken speichert Ecken, die noch nicht am richtigen Ort sind
        # ab, damit sie gelöst werden können.
        
        upperEcken = list(set(self.__whiteEcken).intersection([1,2,3,4]))
        downEcken = []
        for i in range (4,8):
            if "W" in self.__ecken[i] and (self.__ecken[i][1] != "W" or 
                                           len(list(set(["B", "R", "G", "O"]).intersection(self.__ecken[i])
                                           .intersection([["B", "R", "G", "O"][i-5], ["B", "R", "G", "O"][i-4]]))) != 2):
                downEcken.append(i)
        
        # Diese Schleife löst die Ecken. Nach jedem Schritt müssen upperEcken und downEcken wieder angepasst werden. Die 
        # Hauptsächlichen Bewegungen passieren in den __DC (downCorner) Methoden. Die __micro - Methoden werden später auch von anderen 
        # Lösungsschritten benutzt. 
        
        while len(upperEcken) > 0 or len(downEcken) > 0:
            if len(upperEcken)>0:
                self.__DCupperCornerSolve(upperEcken[0])
            
            upperEcken = list(set(self.__whiteEcken).intersection([1,2,3,4]))
            downEcken.clear()
            for i in range (4,8):
                if "W" in self.__ecken[i] and (self.__ecken[i][1] != "W" or 
                                            len(list(set(["B", "R", "G", "O"]).intersection(self.__ecken[i])
                                            .intersection([["B", "R", "G", "O"][i-5], ["B", "R", "G", "O"][i-4]]))) != 2):
                    downEcken.append(i)
            
            if len(downEcken)>0:
                self.__DCdownCornerSolve(downEcken[0])
                self.__curentTeile()
                
                downEcken.clear()
                for i in range (4,8):
                    if "W" in self.__ecken[i] and (self.__ecken[i][1] != "W" or 
                                                len(list(set(["B", "R", "G", "O"]).intersection(self.__ecken[i])
                                                .intersection([["B", "R", "G", "O"][i-5], ["B", "R", "G", "O"][i-4]]))) != 2):
                        downEcken.append(i)
                upperEcken = list(set(self.__whiteEcken).intersection([1,2,3,4]))

    def __DCupperCornerSolve(self, num:int):
        self.__curentTeile()
        num = num - 1
        middles = ["B", "R", "G", "O"]
        betweenMiddles = list(set(middles).intersection(self.__ecken[num]))
        
        
        while not(middles[num%4 - 1] in betweenMiddles and middles[num%4] in betweenMiddles):
            self.cube.seiteDrehen("Y", -1)
            self.__solvehistory.append(("Y", -1))
            self.__curentTeile()
            num = num + 1
        
        if num%4 == 1 or num%4 == 3:
            if self.__ecken[num%4][0] == "W":
                self.__eckeMicro2(middles[num%4 - 1])
            elif self.__ecken[num%4][1] == "W":
                for i in range(0,3):
                    self.__eckeMicroR1(middles[num%4-1])
            else:
                self.__eckeMicroR1(middles[num%4-1])
        else:
            if self.__ecken[num%4][0] == "W":
                self.__eckeMicroR1(middles[num%4-1])
            elif self.__ecken[num%4][1] == "W":
                for i in range(0,3):
                    self.__eckeMicroR1(middles[num%4-1])
            else:
                self.__eckeMicro2(middles[num%4-1])
        self.__curentTeile()

    def __DCdownCornerSolve(self, num:int):
        middles = ["B", "R", "G", "O"]
        self.__eckeMicroR1(middles[num-5])
        self.__curentTeile()
        self.__DCupperCornerSolve(num-3)

    def __eckeMicroR1(self, col):
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
        
        self.__curentTeile()

    def __eckeMicroL1(self, col):
        col = ["B", "R", "G", "O"][["B", "R", "G", "O", "B"].index(col) -1]
        
        self.cube.seiteDrehen(col, -1)
        self.__solvehistory.append((col, -1))
        
        self.cube.seiteDrehen("Y", -1)
        self.__solvehistory.append(("Y", -1))
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen("Y", 1)
        self.__solvehistory.append(("Y", 1))
        
        self.__curentTeile()

    def __eckeMicro2(self, col):
        col = ["B", "R", "G", "O", "B"][["B", "R", "G", "O", "B"].index(col) + 1]
        
        self.cube.seiteDrehen("Y", 1)
        self.__solvehistory.append(("Y", 1))
        
        self.cube.seiteDrehen(col, 1)
        self.__solvehistory.append((col, 1))
        
        self.cube.seiteDrehen("Y", -1)
        self.__solvehistory.append(("Y", -1))
        
        self.cube.seiteDrehen(col, -1)
        self.__solvehistory.append((col, -1))
        
        self.__curentTeile()

# ---------------------------------------------------------Ende untere Ecken---------------------------------------------------------

# ---------------------------------------------------------Anfang mittlere Kanten---------------------------------------------------------

    def solveMidSides(self):
        self.solveDownCorner()
        
        print("________________________________________erste Schicht______________________________________\n")
        print(self.cube.colorPrint())
        print("________________________________________________________________________________________")
        
        middles = ["B", "R", "G", "O"]
        
        upperSide = []
        for i in range(0,4):
            if not "Y" in self.__kanten[i]:
                upperSide.append(i+1)
        
        while len(upperSide)>0:
            self.__MSsolveUpperSide(upperSide[0])
            
            upperSide.clear()
            for i in range(0,4):
                if not "Y" in self.__kanten[i]:
                    upperSide.append(i+1)
        
        middleSide = []
        for i in range(4, 8):
            if i == 4 or i == 6:
                if self.__kanten[i][0] != middles[i-4] and self.__kanten[i][1] != middles[i-5]: middleSide.append(i+1)
            else:
                if self.__kanten[i][0] != middles[i-5] and self.__kanten[i][1] != middles[i-4]: middleSide.append(i+1)
        
        while len(middleSide) > 0:
            self.__MSsolveMidSide(middleSide[0])
            
            middleSide.clear()
            
            for i in range(4, 8):
                if i == 4 or i == 6:
                    if self.__kanten[i][0] != middles[i-4] and self.__kanten[i][1] != middles[i-5]: middleSide.append(i+1)
                else:
                    if self.__kanten[i][0] != middles[i-5] and self.__kanten[i][1] != middles[i-4]: middleSide.append(i+1)
        
        
        print("________________________________________zweite Schicht______________________________________\n")
        print(self.cube.colorPrint())
        print("________________________________________________________________________________________")
    
    def __MSsolveUpperSide(self, num:int):
        self.__curentTeile()
        num = num-1 
        middles = ["B", "R", "G", "O"]
        midCol = self.__kanten[num%4][0]
        
        while middles[num%4] != midCol:
            self.cube.seiteDrehen("Y", -1)
            self.__solvehistory.append(("Y", -1))
            self.__curentTeile()
            num += 1
        
        targetCol = self.__kanten[num%4][1]
        
        if middles[(num+1)%4] == targetCol:
            self.cube.seiteDrehen("Y", 1)
            self.__solvehistory.append(("Y", 1))
            
            self.__eckeMicroR1(midCol)
            self.__eckeMicroL1(targetCol)
            
        else:
            self.cube.seiteDrehen("Y", -1)
            self.__solvehistory.append(("Y", -1))
            
            self.__eckeMicroL1(midCol)
            self.__eckeMicroR1(targetCol)
            
        self.__curentTeile()

    def __MSsolveMidSide(self, num:int):
        middles = ["B", "R", "G", "O"]
        self.__curentTeile()
        self.__eckeMicroR1(middles[num-6])
        
        self.__curentTeile()
        self.__eckeMicroL1(middles[num-5])
        
        self.__curentTeile()
        
        upperSide = []
        for i in range(0,4):
            if not "Y" in self.__kanten[i]:
                upperSide.append(i+1)
        
        while len(upperSide)>0:
            self.__MSsolveUpperSide(upperSide[0])
            
            upperSide.clear()
            for i in range(0,4):
                if not "Y" in self.__kanten[i]:
                    upperSide.append(i+1)


    def __curentKanten(self):
        self.__kanten.clear()
        self.__kanten = [self.cube.getSide(i) for i in range (1,13)]
        
        self.__whiteKanten.clear()
        for i in range(0,12):
            if "W" in self.__kanten[i]:
                self.__whiteKanten.append(i+1)
    
    def __curentEcken(self):
        self.__ecken.clear()
        self.__ecken = self.cube.getCorners()
        
        
        self.__whiteEcken.clear()
        for i in range(0,8):

            if "W" in self.__ecken[i]:
                self.__whiteEcken.append(i+1)
    
    def __curentTeile(self):
        self.__curentEcken()
        self.__curentKanten()
        