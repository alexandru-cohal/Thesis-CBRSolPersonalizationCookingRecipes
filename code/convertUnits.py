unitsList = []
unitsGraph = []

def createGraphUnits():
    global unitsList, unitsGraph

    print("\n ----- Creating the graph of the cooking measurement units ... ----- \n")

    unitsFile = open('units.txt', 'r')
    unitsFileLines = unitsFile.read().splitlines()

    for line in unitsFileLines:
        conversion = line.split(' ')

        quantity1 = float(conversion[0])
        unit1 = conversion[1]

        if unit1 not in unitsList:
            unitsList.append(unit1)
            unitsGraph.append([])

        quantity2 = float(conversion[2])
        unit2 = conversion[3]

        if unit2 not in unitsList:
            unitsList.append(unit2)
            unitsGraph.append([])

        unitsGraph[unitsList.index(unit1)].append((unit2, quantity2 / quantity1))
        unitsGraph[unitsList.index(unit2)].append((unit1, quantity1 / quantity2))

    print("\n ----- Creating the graph of the cooking measurement units DONE ----- \n")


def convertQuantity(quantity1, units1, units2):
    inQueue = [0] * len(unitsList)

    queueQuantity = [(units1, quantity1)]

    if units1 in unitsList:
        inQueue[unitsList.index(units1)] = 1

        while queueQuantity:
            elemQueueQuantity = queueQuantity.pop(0)

            if elemQueueQuantity[0] == units2:
                return elemQueueQuantity[1]

            if elemQueueQuantity[0] in unitsList:
                for conversion in unitsGraph[unitsList.index(elemQueueQuantity[0])]:
                    if inQueue[unitsList.index(conversion[0])] == 0:
                        queueQuantity.append((conversion[0], elemQueueQuantity[1] * conversion[1]))
                        inQueue[unitsList.index(conversion[0])] = 1

    return -1


def main():
    createGraphUnits()


if __name__ == '__main__':
    main()
