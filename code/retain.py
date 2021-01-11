import xml.etree.cElementTree as ET
import xml.dom.minidom as xml

def createXMLNewRecipe(recipeRetrieved, id, replacedIngrName, replacementIngrName, replacementIngrQuantity, stepsAdapted):
    print("\n ----- Generating the XML file for the new recipe ... ----- \n")

    root = ET.Element("recipe")

    ET.SubElement(root, "recipeid").text = str(id)

    ET.SubElement(root, "title").text = recipeRetrieved.name + " Adapted"

    ingredients = ET.SubElement(root, "ingredients")
    for ingredient in recipeRetrieved.ingredients:
        if ingredient.name in replacedIngrName:
            index = replacedIngrName.index(ingredient.name)

            ET.SubElement(ingredients, "ingredient", ingredient=replacementIngrName[index],
                          quantity=str(replacementIngrQuantity[index][0]),
                          unit=replacementIngrQuantity[index][1],
                          qualifiers=""
                          ).text = str(replacementIngrQuantity[index][0]) + " " + replacementIngrQuantity[index][1] + " " + replacementIngrName[index]
        else:
            ET.SubElement(ingredients, "ingredient", ingredient=ingredient.name,
                          quantity=str(ingredient.quantity),
                          unit=ingredient.unit,
                          qualifiers=ingredient.qualifier
                          ).text = str(ingredient.quantity) + " " + ingredient.unit + " " + ingredient.qualifier + " " + ingredient.name

    preparation = ET.SubElement(root, "preparation")
    for step in stepsAdapted:
        ET.SubElement(preparation, "step").text = step

    diet = ET.SubElement(root, "diet")
    for excludedDiet in recipeRetrieved.excludedDiets:
        ET.SubElement(diet, "exclude-for-diet").text = excludedDiet

    tree = ET.ElementTree(root)
    tree.write("newRecipe.xml")

    print("\n ----- Generating the XML file for the new recipe DONE ----- \n")

def updateCaseBase():
    print("\n ----- Updating the recipe case-base ... ----- \n")

    recipeCaseBaseFile = open('ccc_salad.xml', 'r')
    recipeCaseBaseFileLines = recipeCaseBaseFile.read().splitlines()
    del recipeCaseBaseFileLines[-1]
    recipeCaseBaseFile.close()

    newRecipeFile = open('newRecipe.xml', 'r')
    newRecipeFileLines = newRecipeFile.read().splitlines()
    newRecipeFile.close()

    newRecipeCaseBaseFile = open('ccc_salad_v2.xml', 'w')
    for line in recipeCaseBaseFileLines:
        newRecipeCaseBaseFile.write(line)
    for line in newRecipeFileLines:
        newRecipeCaseBaseFile.write(line)
    newRecipeCaseBaseFile.write("</recipes>")
    newRecipeCaseBaseFile.close()

    print("\n ----- Updating the recipe case-base DONE ----- \n")