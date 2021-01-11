# Thesis-CBRSolPersonalizationCookingRecipes
### The thesis developed within the *"Systems and Control"* Masters

- **Date**: June 2017
- **Purpose**: The purpose of my Master's thesis was to develop a solution based on the *Cased-Based Reasoning* approach for recommending an already existent salad recipe from an existent set or creating a slightly modified one such that a lists of desired and unwanted ingredients is satisified. This task represents one the *Salad challenge* proposed within the *Computer Cooking Contest* of the *International Conference on Case-Based Reasoning* held in the year 2017. The given salad recipes and the used food ontology are part of *WikiTaaable*. 
- **Programming Language**: Python
- **Team**: Individual project
- **Inputs**:
  - A set of 68 salad recipes (XML format)
  - An ontology with 2164 culinary ingredients (RDF format)
  - A list of desired ingredient
  - A list of unwanted ingredients
- **Outputs**:
  - A salad recipe which contains the desired ingredients and does not contain the unwanted ingredients
- **Solution**:
  - Based on the *Case-Based Reasoning* approach
  - The following steps are followed:
    - Retrieval: Find a recipe which fits as well as possible the given query based on a similarity function between a salad recipe and the given query (i.e. desired and unwanted ingredients)
    - Reusage: When a perfect match could not be found, perform ingredient adaptation, ingredient quantity adaptation and preparation steps adaptation
    - Revision: The adapted recipe is evaluated by a human expert
    - Retaining: The adapted recipe is stored in the recipe-base if the human expert considers it to be a valuable one
  - For more information about the solution, implementation, results, conclusions and improvements see [this document](documentation/ThesisDocumentation-CBRSolPersonalizationCookingRecipes.pdf) and [this presentation](documentation/ThesisPresentation-CBRSolPersonalizationCookingRecipes.pdf)

