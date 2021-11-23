def parse_equation(equation):
    equation = equation.replace(' ', '')

    parsedEquation = []
    currentNum = ""
    currentPower = "0"
    readingNum = True
    nextNumSign = '-' if equation[0] == '-' else '+'
    numerator = ""
    divisionFlag = False
    i = 0

    while i < len(equation):
        if nextNumSign == '-' and i == 0:
            i+=1
            continue

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
            divisionFlag = False
            numerator = ""

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
            if equation[i + 1] == '-':
                i += 2
            readingNum = False

        elif current == '/':
            divisionFlag = True
            numerator += currentNum
            currentNum = ""
        elif current == 'x' or current == 'X':
            continue
        else:
            return "Invalid"
        i += 1

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
    print(parse_equation("-2/3x^-2 - 3/2"))
