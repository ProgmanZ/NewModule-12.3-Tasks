class DivisionError(Exception):
    pass


with open("numbers.txt", "r") as file:
    for line in file:
        number1, number2 = map(int, line.strip().split())
        try:
            if number1 < number2:
                raise DivisionError
            print(number1 / number2)

        except(DivisionError):
            print('нельзя делить меньшее на большее')
