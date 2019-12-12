# menu-mining
Data Mining project Fall 2019. Looking at connections between regional recipes and regional health. The jupyer notebooks in diseases folder contain the pipeline for disease processing and Data Exploration contains the walk through for results.

List of public food/recipe related data sets: https://hackernoon.com/machine-learning-food-datasets-collection-db21e38ea225

Recipes https://eightportions.com/datasets/Recipes/#fn:1

web_scrape.json was created by scraping https://recipesource.com/ with src/web_scraping.py

WHO data https://www.who.int/healthinfo/global_burden_disease/estimates/en/index1.html

## Data sets: 
  - Recipes scraped from online cooking sites
  - WHO disease burden reports
  - UN import export report
  
## Question:
Mortality/illness have been linked to diet world wide. (ex: https://www.thelancet.com/article/S0140-6736(19)30041-8/fulltext) Can we narrow it down by looking at 
  - types of food: what are the most common foods linked to diseases across countries
  - quantities of food: how many national recipes include these ingredients, how many different types of food are common in the cooking, how much of a specific food is in a recipe eg # of eggs
  - cooking style: frying, baking, grilling, but also marinating, temperature, peeled vs skins, vegetarian vs omnivorous etc etc etc 

Can we find foods/techniques that have low negative impacts and offer replacements by comparing similarly used ingredients?

## Steps:

  ### Data Gathering:
  The src/web_scraping.py file contains the class we created to use Beautiful Soup to scrape https://recipesource.com/

  ### Preprocessing:
  
  1) Recipes: combining multiple data sets, cleaning, looking for data leaks and stop words, tagging and important characteristics extraction.
  2) Countries: clean for illness/mortality that can be tied to food specifically, verifying we have enough countries with recipes to be meaningful, combine over multiple years to try to mitigate potential globalization impact(?)
    
  ### Classificaion step 1
   1) Organized recipes with: Ingredients (including quantity), Cooking Instructions, Nationality classified using a SVM. (src/classifiers/svm)
   
  ### Data Analysis:
   3) By linking terms to illnesses and removing nationalities, look for links between high occurances of foods or cooking types, heats etc with certain illnesses
   
  ### Classification step 2
   1) Classify likely illnesses by recipe terms. We tried both random forest and Logistic Regression One vs Rest to complete this multi label classification. src/classifiers/random_forest and src/classifiers/OVR 
  
   
   
## Tools:
  1) sklearn NLP classification: including vectorizers, SVM, OVR and random forest
  2) Graphing tools: Networkx
  3) Visualization tools: Matplotlib and sns
  4) Data Management: pandas and json
  5) web scraping: beautiful soup
  
