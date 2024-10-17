from functools import total_ordering


class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(5)
num2 = MyNumber(15)

print(5 < 15)  # True

# print(num1 < num2)  # TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)  # True


@total_ordering  # aby działało musza byc co najmniej dwie nadpisane
class MyNumber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num3 = MyNumber2(5)
num4 = MyNumber2(15)
print(num3 < num4)  # True
print(num3 == num4)  # False
print(num3 > num4)  # False
print(num3 >= num4)  # False
num5 = MyNumber2(15)
print(num3 == num5)  # False
print(num4 == num5)  # True
