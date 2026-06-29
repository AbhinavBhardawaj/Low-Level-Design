'''
Static Polymorphism (Compile-time polymorphism) in real life says that
the same action can behave differently depending on the input parameters.
For example, a Manual car can accelerate by a fixed amount or by a
specific amount you request. In programming, we achieve this via method
overloading: multiple methods with the same name but different signatures.
'''


class ManualCar:

    def __init__(self,brand:str,model:str)->None:
        self.__brand = brand
        self.__model = model
        self.__isEngineOn: bool = False
        self.__currentSpeed: int = 0
        self.__currentGear: int = 0
    
    def startEngine(self)->None:
        self.__isEngineOn = True
        print(f"{self.__brand} {self.__model} : Engine started.")

    def stopEngine(self) -> None:
        self.__isEngineOn = False
        self.__currentSpeed = 0
        print(f"{self.__brand} {self.__model} : Engine turned off.")

    # Simulating Method Overloading (Static Polymorphism)
    def accelerate(self, speed: int = 20) -> None:
        if not self.__isEngineOn:
            print(f"{self.__brand} {self.__model} : Cannot accelerate! Engine is off.")
            return

        self.__currentSpeed += speed
        print(f"{self.__brand} {self.__model} : Accelerating to {self.__currentSpeed} km/h")

    def brake(self) -> None:
        self.__currentSpeed -= 20

        if self.__currentSpeed < 0:
            self.__currentSpeed = 0

        print(f"{self.__brand} {self.__model} : Braking! Speed is now {self.__currentSpeed} km/h")

    def shiftGear(self, gear: int) -> None:
        self.__currentGear = gear
        print(f"{self.__brand} {self.__model} : Shifted to gear {self.__currentGear}")


# Main Function
def main() -> None:

    myManualCar: ManualCar = ManualCar("Suzuki", "WagonR")

    myManualCar.startEngine()
    myManualCar.accelerate()       # Equivalent to accelerate()
    myManualCar.accelerate(40)     # Equivalent to accelerate(int)
    myManualCar.brake()
    myManualCar.stopEngine()


if __name__ == "__main__":
    main()