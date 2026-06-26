from abc import ABC, abstractmethod

class Car():

    @abstractmethod
    def startEngine(self):
        pass
    
    @abstractmethod
    def shiftGear(self,gear:int):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def stopEngine(self):
        pass

class SportsCar(Car):

    def __init__(self,b:str,m:str):

        self.brand = b
        self.model = m
        self.isEngineOn = False
        self.currentSpeed = 0
        self.currentGear = 0
    
    def startEngine(self):
        self.isEngineOn = True
        print(f"{self.brand} {self.model}: Engine starts with the roar!")
    
    def shiftGear(self, gear):
        if not self.isEngineOn:
            print(f"{self.brand} {self.model} : Engine is off! Cannot Shift Gear.")
            return

        self.currentGear = gear
        print(f"{self.brand} {self.model} : Shifted to Gear {self.currentGear}.")
    
    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Engine is off! Cannot accelerate.")
            return

        self.current_speed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")

    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0

        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")

    def stopEngine(self):
        self.is_engine_on = False
        self.current_gear = 0
        self.current_speed = 0

        print(f"{self.brand} {self.model} : Engine turned off.")

def main():
    myCar = SportsCar("Rolls Royce","Ghost")
    myCar.startEngine()
    myCar.shiftGear(1)
    myCar.accelerate()
    myCar.shiftGear(2)
    myCar.accelerate()
    myCar.brake()
    myCar.stopEngine()

if __name__ == "__main__":
    main()