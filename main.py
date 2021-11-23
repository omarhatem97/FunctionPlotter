def parse_equation(equation):
    equation = equation.replace(' ', '')

    parsedEquation = {}
    currentNum = ""
    currentPower = "0"
    readingNum = True

    for i in range(len(equation)):
        current = equation[i]

        if is_num(current):
            if readingNum:
                currentNum += current
            else:
                currentPower += current

        elif current == '+':
            parsedEquation[float(currentNum)] = float(currentPower)
            currentNum = ""
            currentPower = "0"

        elif current == '-':
            parsedEquation[float(currentNum)] = -float(currentPower)
            currentNum = ""
            currentPower = "0"

        elif current == '^':
            readingNum = False
        elif current == '/':
            pass
        elif current == 'x' or current == 'X':
            continue
        else:
            return "Invalid"

    if readingNum:
        parsedEquation[float(currentNum)] = 0

    return parsedEquation


# --------------------------------
def is_num(input):
    return '0' <= input <= '9'


if __name__ == '__main__':
    print(parse_equation("2x -  3"))
