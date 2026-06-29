from abc import ABC,abstractmethod

class Car:

    def __init__(self,brand:str, model:str)->None:
        self._brand = brand
        self._model = model
        self._isEngineOn: bool = False
        self._currentSpeed: int = 0
    
    def startEngine(self)->None:
        self._isEngineOn = True
        print(f"{self._brand} {self._model}: Engine started.")

    def stopEngine(self)->None:
        self._isEngineOn = True
        self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Engine turned off.")
    
    @abstractmethod
    def accelerate(self)->None:
        pass

    @abstractmethod
    def accelerate(self, speed:int)->None:
        pass

    @abstractmethod
    def brake(self)->None:
        pass

class ManualCar(Car):

    def __init__(self, brand:str, model:str)->None:
        super().__init__(brand, model)
        self.__currentGear: int = 0
    
    # Specialized method
    def shiftGear(self, gear: int) -> None:
        self.__currentGear = gear
        print(f"{self._brand} {self._model} : Shifted to gear {self.__currentGear}")

    # Dynamic + Static Polymorphism
    def accelerate(self, speed: int = 20) -> None:
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return

        self._currentSpeed += speed

        print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h")

    # Dynamic Polymorphism
    def brake(self) -> None:
        self._currentSpeed -= 20

        if self._currentSpeed < 0:
            self._currentSpeed = 0

        print(f"{self._brand} {self._model} : Braking! Speed is now {self._currentSpeed} km/h")


class ElectricCar(Car):

    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand, model)

        # Private member
        self.__batteryLevel: int = 100

    # Specialized method
    def chargeBattery(self) -> None:
        self.__batteryLevel = 100
        print(f"{self._brand} {self._model} : Battery fully charged!")

    # Dynamic + Static Polymorphism
    def accelerate(self, speed: int = 15) -> None:
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return

        if self.__batteryLevel <= 0:
            print(f"{self._brand} {self._model} : Battery dead! Cannot accelerate.")
            return

        if speed == 15:
            # Equivalent to accelerate()
            self.__batteryLevel -= 10
            self._currentSpeed += 15
        else:
            # Equivalent to accelerate(int speed)
            self.__batteryLevel -= (10 + speed)
            self._currentSpeed += speed

        print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h. Battery at {self.__batteryLevel}%.")

    # Dynamic Polymorphism
    def brake(self) -> None:
        self._currentSpeed -= 15

        if self._currentSpeed < 0:
            self._currentSpeed = 0

        print(f"{self._brand} {self._model} : Regenerative braking! Speed is now {self._currentSpeed} km/h. Battery at {self.__batteryLevel}%.")


# Main Function
def main() -> None:

    myManualCar: Car = ManualCar("Ford", "Mustang")
    myManualCar.startEngine()
    myManualCar.accelerate()
    myManualCar.accelerate()
    myManualCar.brake()
    myManualCar.stopEngine()

    print("----------------------")

    myElectricCar: Car = ElectricCar("Tesla", "Model S")
    myElectricCar.startEngine()
    myElectricCar.accelerate()
    myElectricCar.accelerate()
    myElectricCar.brake()
    myElectricCar.stopEngine()


if __name__ == "__main__":
    main()

