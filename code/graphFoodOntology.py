import parseRDFFoodOntology

ingredientList = []
generalizationList = []
ingredientWeightConversion = []
graphParents = []
graphChildren = []


def getIndexIngredientList(ingredientList, ingredient):
    try:
        return ingredientList.index(ingredient)
    except ValueError:
        return -1


def createGraphFoodOntology():
    print("\n ----- Creating the graph of the food ontology ... ----- \n")

    global graphParents, graphChildren

    for generalization in generalizationList:
        indexIngredientParent = getIndexIngredientList(ingredientList, generalization.parent)
        indexIngredientChild = getIndexIngredientList(ingredientList, generalization.child)
        generalizationCost = generalization.generalizationCost
        graphParents[indexIngredientChild].append((indexIngredientParent, generalizationCost))
        graphChildren[indexIngredientParent].append((indexIngredientChild, generalizationCost))

    print("\n ----- Creating the graph of the food ontology DONE ----- \n")


def lowestCostCommonAncestor(indexIngred1, indexIngred2):
    boundaryIngred1 = [(indexIngred1, 0)]
    queueBoundaryIngred1 = [(indexIngred1, 0)]
    boundaryIngred2 = [(indexIngred2, 0)]
    queueBoundaryIngred2 = [(indexIngred2, 0)]

    LCCAIndex = -1
    LCCACost = 100

    while queueBoundaryIngred1 or queueBoundaryIngred2:

        #Extend Boundary of Ingredient 1
        for index in range(len(queueBoundaryIngred1)):
            elemBoundaryIngred1 = queueBoundaryIngred1.pop(0)

            for parentElemBoundaryIngred1 in graphParents[elemBoundaryIngred1[0]]:
                costParentElemBoundaryIngred1 = elemBoundaryIngred1[1] + parentElemBoundaryIngred1[1]
                boundaryIngred1.append( (parentElemBoundaryIngred1[0], costParentElemBoundaryIngred1) )

                for elemBoundaryIngred2 in boundaryIngred2:
                    if elemBoundaryIngred2[0] == parentElemBoundaryIngred1[0]:
                        if costParentElemBoundaryIngred1 + elemBoundaryIngred2[1] < LCCACost:
                            LCCACost = costParentElemBoundaryIngred1 + elemBoundaryIngred2[1]
                            LCCAIndex = parentElemBoundaryIngred1[0]
                queueBoundaryIngred1.append((parentElemBoundaryIngred1[0], costParentElemBoundaryIngred1))

        #Extend Boundary of Ingredient 2
        for index in range(len(queueBoundaryIngred2)):
            elemBoundaryIngred2 = queueBoundaryIngred2.pop(0)

            for parentElemBoundaryIngred2 in graphParents[elemBoundaryIngred2[0]]:
                costParentElemBoundaryIngred2 = elemBoundaryIngred2[1] + parentElemBoundaryIngred2[1]
                boundaryIngred2.append( (parentElemBoundaryIngred2[0], costParentElemBoundaryIngred2) )

                for elemBoundaryIngred1 in boundaryIngred1:
                    if elemBoundaryIngred1[0] == parentElemBoundaryIngred2[0]:
                        if costParentElemBoundaryIngred2 + elemBoundaryIngred1[1] < LCCACost:
                            LCCACost = costParentElemBoundaryIngred2 + elemBoundaryIngred1[1]
                            LCCAIndex = parentElemBoundaryIngred2[0]
                queueBoundaryIngred2.append((parentElemBoundaryIngred2[0], costParentElemBoundaryIngred2))

    return ingredientList[LCCAIndex], LCCACost


def main():
    global ingredientList, generalizationList, ingredientWeightConversion
    global graphParents, graphChildren

    ingredientList, generalizationList, ingredientWeightConversion = parseRDFFoodOntology.parseRDFFoodOntology()

    graphParents = [[] for index in range(len(ingredientList))]
    graphChildren = [[] for index in range(len(ingredientList))]

    createGraphFoodOntology()

if __name__ == '__main__':
    main()