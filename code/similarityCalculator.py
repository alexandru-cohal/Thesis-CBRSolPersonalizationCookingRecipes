import graphFoodOntology

similarityIngredientsTable = []
noIngredRecipe = 0
noIngredDesired = 0
currentRowsOccupied = []
bestRowsOccupied = []
currentSum = 0
bestSum = 0


def similarityIngredients(ingred1, ingred2):
    indexIngred1 = graphFoodOntology.getIndexIngredientList(graphFoodOntology.ingredientList, ingred1.lower())
    indexIngred2 = graphFoodOntology.getIndexIngredientList(graphFoodOntology.ingredientList, ingred2.lower())

    if indexIngred1 == -1 or indexIngred2 == -1:
        return 0

    LCCA, costLCCA = graphFoodOntology.lowestCostCommonAncestor(indexIngred1, indexIngred2)

    # Convert costLCCA from [0, 2.1] to [1, 0]
    similarity = 1 - (costLCCA / 2.1)

    return similarity


def chooseBestReplacements(indexColumn):
    global currentSum, bestSum
    global currentRowsOccupied, bestRowsOccupied

    # If it is a complete replacement
    if indexColumn == noIngredDesired:
        if currentSum > bestSum:
            bestSum = currentSum
            bestRowsOccupied = list(currentRowsOccupied)
    else:
        for indexRow in range(noIngredRecipe):
            if currentRowsOccupied[indexRow] == -1:
                # Change
                currentRowsOccupied[indexRow] = indexColumn
                currentSum = currentSum + similarityIngredientsTable[indexRow][indexColumn]
                # Move to the next position
                chooseBestReplacements(indexColumn + 1)
                # Change back
                currentSum = currentSum - similarityIngredientsTable[indexRow][indexColumn]
                currentRowsOccupied[indexRow] = -1


def similarityQueryRecipe(desiredIngredientsList, recipe):
    global noIngredRecipe, noIngredDesired
    global currentRowsOccupied, bestRowsOccupied
    global similarityIngredientsTable
    global currentSum, bestSum

    # Initialization
    recipeIngredientsList = [ingredient.name for ingredient in recipe.ingredients]

    noIngredRecipe = len(recipeIngredientsList)
    noIngredDesired = len(desiredIngredientsList)
    currentRowsOccupied = [-1] * noIngredRecipe
    bestRowsOccupied = list([])
    similarityIngredientsTable = list([])
    currentSum = 0
    bestSum = 0

    # Rows - recipe ingredients, Columns - desired ingredients
    similarityIngredientsTable = [[ [] for indexCol in range(noIngredDesired) ] for indexRow in range(noIngredRecipe)]

    for indexRow in range(noIngredRecipe):
        for indexCol in range(noIngredDesired):
            similarityIngredientsTable[indexRow][indexCol] = similarityIngredients(recipeIngredientsList[indexRow], desiredIngredientsList[indexCol])

    # Choose one element from each column (recipe ingredient) such that the rows do not repeat and the maximum sum (similarity) is obtained
    chooseBestReplacements(0)

    # Create the replacement list
    replacedIngredients = []
    for indexIngredDesired in range(noIngredDesired):
        replacedIngredients.append(recipeIngredientsList[bestRowsOccupied.index(indexIngredDesired)])

    return bestSum, replacedIngredients


def main():
    graphFoodOntology.main()


if __name__ == '__main__':
    main()
