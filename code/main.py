import retrieveRecipe
import adaptation
import retain


def main():
    retrieveRecipe.main()

    recipeRetrieved, replacedIngredRecipeRetrieved, replacementsIngredRecipeRetrieved = retrieveRecipe.retrieveRecipe()

    if replacedIngredRecipeRetrieved:
        print("\n", recipeRetrieved.name, "Adapted")
        print("\n", "Ingredients changed:")
        for index in range(len(replacedIngredRecipeRetrieved)):
            print(replacedIngredRecipeRetrieved[index], "->", replacementsIngredRecipeRetrieved[index])

        print("\n", "The new ingredients and their quantities:")
        replacedIngredientQuantity, replacementIngredientQuantity = adaptation.quantityAdaptation(recipeRetrieved, replacedIngredRecipeRetrieved, replacementsIngredRecipeRetrieved)
        for index in range(len(replacedIngredRecipeRetrieved)):
            print(replacedIngredientQuantity[index], replacedIngredRecipeRetrieved[index], "->", replacementIngredientQuantity[index], replacementsIngredRecipeRetrieved[index])

        print("\n", "The new cooking steps:")
        stepsAdapted = adaptation.stepsAdaptation(recipeRetrieved, replacedIngredRecipeRetrieved, replacementsIngredRecipeRetrieved)
        print(stepsAdapted)

        retain.createXMLNewRecipe(recipeRetrieved, len(retrieveRecipe.recipeList) + 100, replacedIngredRecipeRetrieved, replacementsIngredRecipeRetrieved, replacementIngredientQuantity, stepsAdapted)

        update = input("\n" + "Update the recipe case-base with the new recipe? (y/n) ")
        while update not in ("y", "n"):
            update = input("\n" + "Incorrect answer. Update the recipe case-base with the new recipe? (y/n) ")
        if update == "y":
            retain.updateCaseBase()
    else:
        retain.createXMLNewRecipe(recipeRetrieved, recipeRetrieved.id, [], [], [], recipeRetrieved.steps)
        print("No case-base update needed")

    print()

if __name__ == '__main__':
    main()
