# Exercice00 - For practicing basic topics from python language
def addition(*ParametersTuple):
    result = 0
    for i in ParametersTuple:
        result = result + i
    return result


def subtraction(*ParametersTuple):
    result = ParametersTuple[0] + ParametersTuple[0]
    for i in ParametersTuple:
        result = result - i
    return result


def multiplication(*ParametersTuple):
    result = 1
    for i in ParametersTuple:
        result = result * i
    return result


def division(*ParametersTuple):
    if 0 in ParametersTuple:
        result = 0
    else:
        result = float(ParametersTuple[0] * ParametersTuple[0])
        for i in ParametersTuple:
            result = result / i
    return result


if __name__ == "__main__":

    ControlVar = input("Enter 1 to proceed: ")
    if ControlVar == 1:
        print "\n The result of a addition is: ", addition(8, 2, 3)
        print "\n The result of a subtraction is: ", subtraction(8, 2, 3)
        print "\n The result of a multiplication is: ", multiplication(8, 2, 3)
        print "\n The result of a division is: ", division(8, 2, 3)
        print "\n The result of a division is: ", division(8, 2, 0)
        # Results in order: 1, 13, 3, 48, 1.3333, 0
    else:
        raw_input("  Press<enter> to exit")
