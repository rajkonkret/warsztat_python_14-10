class Boat:
    def __init__(self, model, year):
        # __speed - pole prywatne
        self.__speed = 0
        self.model = model
        self.year = year

    def sail(self):
        self.__speed += 10
        self.__test()

    def speedometer(self):
        print(f"Speed in knots {self.__speed}")

    # metoda prywatna
    def __test(self):
        print("All tested")


boat = Boat("Maxus", 2024)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# po oznaczeniu tego pola jako prywatne
# AttributeError: 'Boat' object has no attribute '__speed'
# print(boat.__speed)  # 50
boat.speedometer()  # Speed in knots 50
boat.__speed = 0  # robimy pole o tej samej nazwie ale publiczne
boat.speedometer()  # Speed in knots 0, prędkosc nadal Speed in knots 50 po oznaczeniu pola jako prywatne
print(boat.__speed)  # 0
# All tested
# All tested
# All tested
# All tested
# All tested
# Speed in knots 50
# Speed in knots 50
# 0
# Enkapsulacja - hermetyzownie pól i wystawianie metod do ich odczytu i zmiany
