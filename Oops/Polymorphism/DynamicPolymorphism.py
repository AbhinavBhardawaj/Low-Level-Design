from abc import ABC, abstractmethod

'''
Dynamic Polymorphism in real life says that 2 Objects coming from same
family will respond to same stimulus differently. Like in real world Manual
car and Electric car will respond to accelerate() differently.

To represent this in programming, we create a parent class that defines all
characters and behaviours that are generic to all child classes and are also same in
all child classes but make those methods abstract(virtual) that are generic to all
child classes but all child class will behave differently. Then those child class
will provide implementation details of these abstract methods the way they want.
'''

class Car(ABC):

    def __init__(self, brand:str, model:str):
        self._brand = brand
        self._model = model
        self._isEngineOn: bool = False
        self._currentSpeed: int = 0
    
    # Common methods for all cars
    def startEngine(self)->None:
        self._isEngineOn = True
        print(f"{self._brand} {self._model} : Engine started.")
    
    def stopEngine(self)->None:
        self._isEngineOn = False
        self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Engine turned off.")

    # Abstract methods for dynamic polymorphism
    @abstractmethod
    def accelerate(self)->None:
        pass

    @abstractmethod
    def brake(self)->None:
        pass

class ManualCar(Car):

    def __init__(self, brand:str, model:str)->None:
        super().__init__(brand, model)
        self.__currentGear:int = 0
    
    # Specialized only for Manual car
    def shiftGear(self,gear:int)->None:
        self.__currentGear = gear
        print(f"{self._brand} {self._model} : Shifted to gear {self.__currentGear}")
    
    # Overriding accelerate - Dynamic Polymorphism
    def accelerate(self)->None:
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return

        self._currentSpeed += 20
        print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h")
    
    # Overriding brake - Dynamic Polymorphism
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

    # Specialized method for Electric Car
    def chargeBattery(self) -> None:
        self.__batteryLevel = 100
        print(f"{self._brand} {self._model} : Battery fully charged!")

    # Overriding accelerate - Dynamic Polymorphism
    def accelerate(self) -> None:
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return

        if self.__batteryLevel <= 0:
            print(f"{self._brand} {self._model} : Battery dead! Cannot accelerate.")
            return

        self.__batteryLevel -= 10
        self._currentSpeed += 15

        print(
            f"{self._brand} {self._model} : Accelerating to "
            f"{self._currentSpeed} km/h. Battery at {self.__batteryLevel}%."
        )

    # Overriding brake - Dynamic Polymorphism
    def brake(self) -> None:
        self._currentSpeed -= 15

        if self._currentSpeed < 0:
            self._currentSpeed = 0

        print(
            f"{self._brand} {self._model} : Regenerative braking! "
            f"Speed is now {self._currentSpeed} km/h. "
            f"Battery at {self.__batteryLevel}%."
        )


# Main Function
def main() -> None:

    myManualCar: Car = ManualCar("Suzuki", "WagonR")
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