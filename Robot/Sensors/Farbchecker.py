class Farbchecker:
    """
    ### Mit dieser Klasse werden die Farben des Würfels mithilfe von zwei Methoden eingelesen. 
    #### Es gibt:
    - rubColWArea(r,g,b)
    - rubColWDiff(r,g,b)
    """
    def __init__(self):
        
        # Absolute Angaben der Zahlen:
        
        self.farben = {"R": [50, 28, 55],
                             "Y": [10, 12, 45],
                             "O": [61, 78, 100],
                             "W": [77, 89, 100],
                             "B": [18, 63, 100],
                             "G": [24, 54, 100]}
        
        # Farbbereiche. Bsp bei Rot: Index 0 -> Untergrenze Rot, 1 -> Obergrenze Rot, 2 -> Untergrenze Grün, 3 -> Obergrenze Grün usw. 
        
        self.farbbereiche = {}
        
        for key in self.farben:
            self.farbbereiche[key] = []    
            for i in range(0,3):
                if self.farben[key][i]-10 >= 0: self.farbbereiche[key].append(self.farben[key][i] - 10)
                else: self.farbbereiche[key].append(0)
                if self.farben[key][i]+10 <= 100: self.farbbereiche[key].append(self.farben[key][i] + 10)
                else: self.farbbereiche[key].append(100)


    def rubColWArea(self, r:int, g:int, b:int):
        """Diese Methode benutzt die Farbbereiche, um eine Farbe zu ermitteln. Wenn die Farbe in keinem Bereich ist, dann wird die Farbe ausgegeben, welche bei
        self.rubColWDif() mit denselben Werten herauskommt"""
        
        for key in self.farbbereiche:
            ber = self.farbbereiche[key]                #Dies gilt nur für die Abkürzung, ansonsten wäre die nächste Zeile sehr lang 
            if r > ber[0] and r < ber[1] and g > ber[2] and g < ber[3] and b > ber[4] and b < ber[5]:
                return key
        
        # Wenn die Farbe in keinem Bereich ist, dann wird mit rebColWDif gearbeitet.
        
        return self.rubColWDif(r,g,b)
    
    def rubColWDif(self, r:int, g:int, b:int) -> str:
        # closestDif auf 300, weil das die größtmögliche Differenz ist, es kann also nur besser sein
        
        closestCol = ""
        closestDif = 300
        
        for key in self.farben.keys():
            dif = 0
        
        # Betrag von Differenz zwischen r Bereich der eingegebenen Farbe und der eingestellten Farbe. Dasselbe für b und g
        
            dif += abs(self.farben[key][0] - r) + abs(self.farben[key][1] - g) + abs(self.farben[key][2] - b)
            if dif < closestDif: 
                closestDif = dif
                closestCol = key

        return closestCol
        
    def __str__(self) -> str:
        out = ""
        for key in self.farben:
            out += key + " -> "
            for item in self.farben[key]:
                out += str(item) + " | "
            out += "\n"
        
        return out