# Last updated: 12/6/2025, 5:40:53 am
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.carSlot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.carSlot[carType-1] >= 1:
            self.carSlot[carType-1] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)