
def parseTXTQuery():
    print("\n ----- Parsing query TXT file query.txt ... ----- \n")

    queryFile = open('query.txt', 'r')
    queryFileLines = queryFile.read().splitlines()

    desiredIngredients = queryFileLines[0].split(' ')

    undesiredIngredients = queryFileLines[1].split(' ')

    queryFile.close()

    print("\n ----- Parsing query TXT file query.txt DONE ----- \n")

    return desiredIngredients, undesiredIngredients
