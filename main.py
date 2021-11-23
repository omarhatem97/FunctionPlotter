def parse_equation(equation):
    equation = equation.replace(' ', '')

    parsedEquation = []
    currentNum = ""
    currentPower = "0"
    readingNum = True
    nextNumSign = '+'
    numerator = ""
    denomenator = ""
    divisionFlag = False

    for i in range(len(equation)):
        current = equation[i]

        if is_num(current):
            if readingNum:
                currentNum += current
            else:
                currentPower += current

        elif current == '+':
            if nextNumSign == '+':
                parsedEquation.append((float(currentNum), float(currentPower)))
            else:
                parsedEquation.append((-float(currentNum), float(currentPower)))
            currentNum = ""
            currentPower = "0"
            nextNumSign = '+'
            readingNum = True

        elif current == '-':
            if divisionFlag:
                currentNum = float(numerator) / float(currentNum)

            if nextNumSign == '+':
                parsedEquation.append((float(currentNum), float(currentPower)))
            else:
                parsedEquation.append((-float(currentNum), float(currentPower)))
            currentNum = ""
            currentPower = "0"
            nextNumSign = '-'
            readingNum = True
            divisionFlag = False
            numerator = ""

        elif current == '^':
            readingNum = False

        elif current == '/':
            divisionFlag = True
            numerator += currentNum
            currentNum = ""
        elif current == 'x' or current == 'X':
            continue
        else:
            return "Invalid"

    if readingNum:
        if divisionFlag:
            currentNum = float(numerator) / float(currentNum)
        if nextNumSign == '+':
            parsedEquation.append((float(currentNum), float(currentPower)))
        else:
            parsedEquation.append((-float(currentNum), float(currentPower)))

    return parsedEquation


# --------------------------------
def is_num(input):
    return '0' <= input <= '9'


if __name__ == '__main__':
    print(parse_equation("2/3x^2 -  3/2"))
