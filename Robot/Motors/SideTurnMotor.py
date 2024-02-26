
from AdvMotor import AdvMotor

class SideTurnMotor(AdvMotor):
    
    def __init__(self, port: str) -> None:
        super().__init__(port)
        self.drehungWinkel = 105
        self.drehungGeschwindigkeit = -400     

        