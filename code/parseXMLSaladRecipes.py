# Parse the salad recipes XML file ccc_salad.xml. Return a list of recipes (Recipe objects).

import xml.etree.ElementTree as ET


class Ingredient:
    def __init__(self, name, quantity, unit, qualifier):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.qualifier = qualifier

    def __str__(self):
        return str(self.quantity) + " " + self.unit + " " + self.name + " " + self.qualifier


class Recipe:
    def __init__(self, number, name, ingredients, steps, excludedDiets):
        self.id = number
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.excludedDiets = excludedDiets

    def __str__(self):
        return self.name


def parseXMLSaladRecipes():
    print("\n ----- Parsing salad recipes XML file ccc_salad.xml ... ----- \n")

    tree = ET.parse('ccc_salad.xml')
    root = tree.getroot()

    recipeList = []
    for recipe in root:

        # 'recipeid' element
        recipeID = recipe[0].text

        # 'title' element
        recipeName = recipe[1].text

        # 'ingredients' element ('ingredient' elements)
        recipeIngredients = []
        for ingredientXmlElem in recipe[2]:
            ingredientObj = Ingredient(ingredientXmlElem.attrib['ingredient'],
                                       float(ingredientXmlElem.attrib['quantity']) if ingredientXmlElem.attrib['quantity'] != "" else 0,
                                       ingredientXmlElem.attrib['unit'],
                                       ingredientXmlElem.attrib['qualifiers'])
            recipeIngredients.append(ingredientObj)

        # 'preparation' element ('step' elements)
        recipeSteps = []
        for step in recipe[3]:
            recipeSteps.append(step.text)

        # 'diet' element ('exclude-for-diet' elements)
        recipeDiets = []
        for diet in recipe[4]:
            recipeDiets.append(diet.text)

        recipeObj = Recipe(recipeID, recipeName, recipeIngredients, recipeSteps, recipeDiets)

        recipeList.append(recipeObj)

    print("\n ----- Parsing salad recipes XML file ccc_salad.xml DONE ----- \n")

    return recipeList
