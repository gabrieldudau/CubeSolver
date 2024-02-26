from Robot.Motors.AdvMotor import AdvMotor

class SidePushMotor(AdvMotor):
    
    def __init__(self, port) -> None:
        super().__init__(port)
        
        self.drehungWinkel = 40
        self.drehungGeschwindigkeit = 100

    def pushTo_FromCube(self, speed):
        """positive Speed bewegt den Motor zum Cube und negative weg davon"""
        self.motor.run_until_stalled(speed)
    
    
        