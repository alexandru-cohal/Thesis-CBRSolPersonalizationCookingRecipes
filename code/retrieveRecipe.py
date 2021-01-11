import parseXMLSaladRecipes as parseXMLRecipes
import parseTXTQuery as parseTXTQuery
import similarityCalculator as similarity

desiredIngredientsList = []
undesiredIngredientsList = []
recipeList = []

def retrieveRecipe():
    # Select those recipes which does not have any unwanted ingredient => recipeCandidateList
    # Verify if exists any recipe which matches all restrictions => recipeMatch
    recipeCandidateList = []
    recipeMatch = None

    for recipe in recipeList:
        recipeIngredientsName = [ingredient.name for ingredient in recipe.ingredients]
        if len(set(recipeIngredientsName).intersection(set(undesiredIngredientsList))) == 0:
            recipeCandidateList.append(recipe)
            if len(set(recipeIngredientsName).intersection(set(desiredIngredientsList))) == len(desiredIngredientsList):
                recipeMatch = recipe
                break

    # If there is not any perfect match, analyze the remaining candidates
    if recipeMatch is None:
        print("No perfect match.", len(recipeCandidateList), "candidates remaining.")

        valueMaxRecipeSimilarity = 0
        recipeMaxRecipeSimilarity = None
        for recipe in recipeCandidateList:
            #Compute the similarity level between the query and the selected recipe
            valueSimilarity, replacedIngredients = similarity.similarityQueryRecipe(desiredIngredientsList, recipe)
            #Determine the recipe with maximum similarity
            if valueSimilarity > valueMaxRecipeSimilarity:
                valueMaxRecipeSimilarity = valueSimilarity
                recipeMaxRecipeSimilarity = recipe
                replacedIngredientsMaxRecipeSimilarity = replacedIngredients

        return recipeMaxRecipeSimilarity, replacedIngredientsMaxRecipeSimilarity, desiredIngredientsList
    else:
        #There is a perfect match
        print("Perfect match: ", recipeMatch)
        return recipeMatch, [], desiredIngredientsList


def main():
    global desiredIngredientsList, undesiredIngredientsList
    global recipeList

    desiredIngredientsList, undesiredIngredientsList = parseTXTQuery.parseTXTQuery()
    recipeList = parseXMLRecipes.parseXMLSaladRecipes()

    similarity.main()


if __name__ == '__main__':
    main()
