class Car:

    def __init__(self, brand: str, model: str) -> None:
        self.brand: str = brand
        self.model: str = model
        self.isEngineOn: bool = False
        self.currentSpeed: int = 0

    # Common methods for all cars.
    def startEngine(self) -> None:
        self.isEngineOn = True
        print(f"{self.brand} {self.model} : Engine started.")

    def stopEngine(self) -> None:
        self.isEngineOn = False
        self.currentSpeed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")

    def accelerate(self) -> None:
        if not self.isEngineOn:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return

        self.currentSpeed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.currentSpeed} km/h")

    def brake(self) -> None:
        self.currentSpeed -= 20
        if self.currentSpeed < 0:
            self.currentSpeed = 0

        print(f"{self.brand} {self.model} : Braking! Speed is now {self.currentSpeed} km/h")


class ManualCar(Car):  # Inherits from Car

    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand, model)
        self.currentGear: int = 0

    # Specialized method for Manual Car
    def shiftGear(self, gear: int) -> None:
        self.currentGear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.currentGear}")


class ElectricCar(Car):  # Inherits from Car

    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand, model)
        self.batteryLevel: int = 100

    # Specialized method for Electric Car
    def chargeBattery(self) -> None:
        self.batteryLevel = 100
        print(f"{self.brand} {self.model} : Battery fully charged!")


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