import retrieveRecipe
import convertUnits


def quantityAdaptation(recipeRetrieved, replacedIngredRecipeRetrieved, replacementsIngredRecipeRetrieved):
    foodOntologyIngrList = retrieveRecipe.similarity.graphFoodOntology.ingredientList
    foodOntologyIngrWeightConversion = retrieveRecipe.similarity.graphFoodOntology.ingredientWeightConversion

    convertUnits.main()

    replacedIngredientQuantity = []
    replacementIngredientQuantity = []
    for index in range(len(replacedIngredRecipeRetrieved)):
        for ingredient in recipeRetrieved.ingredients:
            if replacedIngredRecipeRetrieved[index] == ingredient.name:
                replacedIngrName = ingredient.name
                replacedIngrQuantity = ingredient.quantity
                replacedIngrUnit = ingredient.unit
                if replacedIngrUnit == "":
                    replacedIngrUnit = "unit"
                replacedIngrQualifier = ingredient.qualifier
                replacedIngrWeightConversion = foodOntologyIngrWeightConversion[foodOntologyIngrList.index(replacedIngrName)]
                break

        replacedIngredientQuantity.append((replacedIngrQuantity, replacedIngrUnit))

        replacementIngrName = replacementsIngredRecipeRetrieved[index]
        replacementIngrWeightConversion = foodOntologyIngrWeightConversion[foodOntologyIngrList.index(replacementIngrName)]

        if replacedIngrName != replacementIngrName:
            if replacedIngrUnit != "g":
                replacedIngrQuantityGrams = 0
                for weightConversion in replacedIngrWeightConversion:
                    if weightConversion[1] == replacedIngrUnit or (replacedIngrUnit == "unit" and weightConversion[1] == ""):
                        replacedIngrQuantityGrams = (replacedIngrQuantity * weightConversion[3]) / weightConversion[0]
                        break
                if replacedIngrQuantityGrams == 0:
                    replacedIngrQuantityGrams = convertUnits.convertQuantity(replacedIngrQuantity, replacedIngrUnit, "g")

            if replacementIngrWeightConversion:
                maxReplacementIngrQuantity = -1

                for weightConversion in replacementIngrWeightConversion:
                    replacementIngrQuantity = (replacedIngrQuantityGrams * weightConversion[0]) / weightConversion[3]

                    if replacementIngrQuantity > maxReplacementIngrQuantity or maxReplacementIngrQuantity == -1:
                        maxReplacementIngrQuantity = replacementIngrQuantity
                        weightConversionMax = weightConversion

                replacementIngrQuantity = round((replacedIngrQuantityGrams * weightConversionMax[0]) / weightConversionMax[3], 1)
                replacementIngrUnit = weightConversionMax[1]

                replacementIngredientQuantity.append((replacementIngrQuantity, replacementIngrUnit))
        else:
            replacementIngredientQuantity.append((replacedIngrQuantity, replacedIngrUnit))

    return replacedIngredientQuantity, replacementIngredientQuantity


def stepsAdaptation(recipeRetrieved, replacedIngredRecipeRetrieved, replacementsIngredRecipeRetrieved):
    stepsAdapted = []
    for step in recipeRetrieved.steps:
        for replacedIngredient, replacementIngredient in zip(replacedIngredRecipeRetrieved, replacementsIngredRecipeRetrieved):
            step = step.replace(replacedIngredient, replacementIngredient)
            step = step.replace(replacedIngredient.replace('_', ' '), replacementIngredient)
        stepsAdapted.append(step)

    return stepsAdapted
