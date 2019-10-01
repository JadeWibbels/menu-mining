# menu-mining
Data Mining project Fall 2019. Looking at connections between regional recipes and regional health.

List of public food/recipe related data sets: https://hackernoon.com/machine-learning-food-datasets-collection-db21e38ea225

Recipes https://eightportions.com/datasets/Recipes/#fn:1

WHO data https://www.who.int/healthinfo/global_burden_disease/estimates/en/index1.html

## Data sets: 
  - Recipes scraped from online cooking sites
  - WHO disease burden reports
  - UN import export report
  
## Question:
Mortality/illness have been linked to diet world wide. (ex: https://www.thelancet.com/article/S0140-6736(19)30041-8/fulltext) Can we narrow it down by looking at 
  - types of food: what are the most common foods linked to diseases across countries
  - quantities of food: how many national recipes include these ingredients, how many different types of food are common in the cooking, how much of a specific food is in a recipe eg # of eggs
  - cooking style: frying, baking, grilling, but also marinating, temperature

Can we find foods/techniques that have low negative impacts and offer replacements by comparing similarly used ingredients?

Steps:
   1) Organize recipes with: Ingredients (including quantity), Cooking Instructions, Nationality (will use classification)
   2) Organize Countries with population, illnesses, Cause of Death, Imports and Exports
   3) Look for links between high occurances of foods or cooking types, heats etc with certain illnesses
   4) Look for potential low risk replacement foods/processes by finding similar types of recipes with different ingredients.


