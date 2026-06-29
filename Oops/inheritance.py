class Car:

    def __init__(self, brand: str, model: str) -> None:
        self._brand = brand
        self._model = model
        self._isEngineOn: bool = False
        self._currentSpeed: int = 0

    # Common methods for all cars.
    def startEngine(self) -> None:
        self._isEngineOn = True
        print(f"{self._brand} {self._model} : Engine started.")

    def stopEngine(self) -> None:
        self._isEngineOn = False
        self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Engine turned off.")

    def accelerate(self) -> None:
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return

        self._currentSpeed += 20
        print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h")

    def brake(self) -> None:
        self._currentSpeed -= 20
        if self._currentSpeed < 0:
            self._currentSpeed = 0

        print(f"{self._brand} {self._model} : Braking! Speed is now {self._currentSpeed} km/h")


class ManualCar(Car):  # Inherits from Car

    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand, model)
        self.__CurrentGear: int = 0

    # Specialized method for Manual Car
    def shiftGear(self, gear: int) -> None:
        self.__CurrentGear = gear
        print(f"{self._brand} {self._model} : Shifted to gear {self.__CurrentGear}")


class ElectricCar(Car):  # Inherits from Car

    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand, model)
        self.__batteryLevel: int = 100

    # Specialized method for Electric Car
    def chargeBattery(self) -> None:
        self.__batteryLevel = 100
        print(f"{self._brand} {self._model} : Battery fully charged!")


# Main Method
def main() -> None:

    myManualCar: ManualCar = ManualCar("Suzuki", "WagonR")
    myManualCar.startEngine()
    myManualCar.shiftGear(1)  # specific to manual car
    myManualCar.accelerate()
    myManualCar.brake()
    myManualCar.stopEngine()

    print("----------------------")

    myElectricCar: ElectricCar = ElectricCar("Tesla", "Model S")
    myElectricCar.chargeBattery()  # specific to electric car
    myElectricCar.startEngine()
    myElectricCar.accelerate()
    myElectricCar.brake()
    myElectricCar.stopEngine()


if __name__ == "__main__":
    main()