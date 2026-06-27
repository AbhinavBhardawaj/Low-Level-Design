class SportsCar:

    def __init__(self, brand:str, model:str) -> None:
        self.__brand = brand
        self.__model = model
        self.__isEngineOn: bool = False
        self.__currentSpeed: int = 0
        self.__currentGear: int = 0

        # Introducing new variable to explain setters
        self.__tyreCompany = "MRF"

    def getSpeed(self)->int:
        return self.__currentSpeed
    
    def getTyreCompany(self)->str:
        return self.__tyreCompany
    
    def setTyreCompany(self, tyreCompany:str)->None:
        self.__tyreCompany = tyreCompany
    
    def startEngine(self)->None:
        self.__isEngineOn = True
        print(f"{self.__brand} {self.__model} : Engine starts with a roar!")
    
    def shiftGear(self,gear:int)->None:
        if not self.__isEngineOn:
            print(f"{self.__brand} {self.__model} : Engine is off! Cannot Shift Gear.")
            return

        self.__currentGear = gear
        print(f"{self.__brand} {self.__model} : Shifted to gear {self.__currentGear}")

    def accelerate(self)->None:
        if not self.__isEngineOn:
            print(f"{self.__brand} {self.__model} : Engine is off! Cannot accelerate.")
            return

        self.__currentSpeed += 20
        print(f"{self.__brand} {self.__model} : Accelerating to {self.__currentSpeed} km/h")

    def brake(self)->None:
        self.__currentSpeed -= 20
        if self.__currentSpeed < 0:
            self.__currentSpeed = 0

        print(f"{self.__brand} {self.__model} : Braking! Speed is now {self.__currentSpeed} km/h")

    def stop_engine(self)->None:
        self.__isEngineOn = False
        self.__currentGear = 0
        self.__currentSpeed = 0

        print(f"{self.__brand} {self.__model} : Engine turned off.")


# Main Method
def main():

    mySportsCar = SportsCar("Ford", "Mustang")

    mySportsCar.startEngine()
    mySportsCar.shiftGear(1)
    mySportsCar.accelerate()
    mySportsCar.shiftGear(2)
    mySportsCar.accelerate()
    mySportsCar.brake()
    mySportsCar.stop_engine()

    # Setting arbitrary value to speed (Not allowed due to encapsulation)
    # mySportsCar.__currentSpeed = 500

    # print("Current Speed of My Sports Car is set to",
    #       mySportsCar.__currentSpeed)

    print("Current Speed of My Sports Car is",
          mySportsCar.getSpeed())


if __name__ == "__main__":
    main()

    