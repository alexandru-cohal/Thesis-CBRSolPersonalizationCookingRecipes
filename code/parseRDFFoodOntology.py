# Parse the food ontology RDF file food.rdf. Return a list of generalization relations (GeneralizationRelation objects).

import xml.etree.ElementTree as ET

URI_OWL = "{http://www.w3.org/2002/07/owl#}"
URI_RDF_SYNTAX = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
URI_RDF_SCHEMA = "{http://www.w3.org/2000/01/rdf-schema#}"
URI_CATEGORY = "http://wikitaaable.loria.fr/index.php/Special:URIResolver/Category-3A"
URI_PROPERTY = "{http://wikitaaable.loria.fr/index.php/Special:URIResolver/Property-3A}"


class GeneralizationRelation:
    def __init__(self, parent, child, generalizationCost):
        self.parent = parent
        self.child = child
        self.generalizationCost = float(generalizationCost)

    def __str__(self):
        return self.parent + " generalizes " + self.child + " with cost " + str(self.generalizationCost)


def parseRDFFoodOntology():
    print("\n ----- Parsing food ontology RDF file food.rdf ... ----- \n")

    tree = ET.parse('food.rdf')
    root = tree.getroot()

    ingredientList = []
    generalizationList = []
    ingredientWeightConversion = []
    for ingredientClass in root:

        if ingredientClass.tag == URI_OWL + 'Class':

            # 'about' attribute
            ingredientAbout = ingredientClass.attrib[URI_RDF_SYNTAX + 'about'].replace(URI_CATEGORY, "").lower()
            ingredientList.append(ingredientAbout)
            ingredientWeightConversion.append([])

            # 'label' element
            ingredientLabel = ingredientClass.find(URI_RDF_SCHEMA + 'label')
            if ingredientLabel is not None:
                ingredientLabel = ingredientLabel.text.lower()
            else:
                ingredientLabel = ""

            # 'subClassOf' elements
            parentsElements = ingredientClass.findall(URI_RDF_SCHEMA + 'subClassOf')
            ingredientParents = []
            for parent in parentsElements:
                ingredientParents.append(parent.attrib[URI_RDF_SYNTAX + 'resource'].replace(URI_CATEGORY, "").lower())

            # 'Has_generalisation_cost' elements ('Generalisation_class' and 'Generalisation_cost' elements)
            generalizationsElements = ingredientClass.findall(URI_PROPERTY + 'Has_generalisation_cost')
            ingredientGeneralizations = {}
            for generalisation in generalizationsElements:
                generalizationParent = generalisation[0].find(URI_PROPERTY + 'Generalisation_class').attrib[URI_RDF_SYNTAX + 'resource'].replace(URI_CATEGORY, "").lower()
                generalizationCost = generalisation[0].find(URI_PROPERTY + 'Generalisation_cost').text
                ingredientGeneralizations[generalizationParent] = generalizationCost

            for parent in ingredientParents:
                if parent in ingredientGeneralizations:
                    generalizationObj = GeneralizationRelation(parent, ingredientAbout, ingredientGeneralizations[parent])
                else:
                    generalizationObj = GeneralizationRelation(parent, ingredientAbout, 0)
                generalizationList.append(generalizationObj)

            # 'WeightConversion' elements
            conversionElements = ingredientClass.findall(URI_PROPERTY + 'Weight_conversion')
            for conversion in conversionElements:
                conversionFinalQuantity = float(conversion[0].find(URI_PROPERTY + 'Final_quantity').text)
                conversionOriginalQuantity = float(conversion[0].find(URI_PROPERTY + 'Original_quantity').text)
                conversionFinalUnit = "g"

                try:
                    conversionQualifier = conversion[0].find(URI_PROPERTY + 'Qualifiers').text.lower()
                except:
                    conversionQualifier = ""

                try:
                    conversionOriginalUnit = conversion[0].find(URI_PROPERTY + 'Original_unit').text.lower()
                except:
                    conversionOriginalUnit = "unit"

                ingredientWeightConversion[-1].append((conversionOriginalQuantity, conversionOriginalUnit, conversionQualifier, conversionFinalQuantity, conversionFinalUnit))

    print("\n ----- Parsing food ontology RDF file food.rdf DONE ----- \n")

    return ingredientList, generalizationList, ingredientWeightConversion
