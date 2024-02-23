class Farbchecker:
    def __init__(self):
        self.farbbereiche = {"R": [50, 28, 55],
                             "Y": [10, 12, 45],
                             "O": [61, 78, 100],
                             "W": [77, 89, 100],
                             "B": [18, 63, 100],
                             "G": [24, 54, 100]}
    
    def getRubicsColor(self, r:int, g:int, b:int) -> str:
        closestCol = ""
        closestDif = 300
        for key in self.farbbereiche.keys():
            dif = 0
            dif += abs(self.farbbereiche[key][0] - r) + abs(self.farbbereiche[key][1] - g) + abs(self.farbbereiche[key][2] - b)
            if dif < closestDif: 
                closestDif = dif
                closestCol = key

        return closestCol
        
    def __str__(self) -> str:
        out = ""
        for key in self.farbbereiche.keys():
            out += key + " -> "
            for item in self.farbbereiche[key]:
                out += str(item) + " | "
            out += "\n"
        return out