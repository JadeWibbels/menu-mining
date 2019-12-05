import json

from src.utils.normal_terms import normal_terms

class Cuisine:
    
    def __init__(self, countries):
        self.countries = countries
        self.cookbook = {'recipes': [],
                         'cuisine': []}

        self.cuisine_id = {'greek': ['greek', 'greece'],
                           'filipino': ['filipino', 'philippines', 'pancit', 'adobo'],
                           'russian':['russian', 'russia'], 
                           'french': ['france', 'french'],
                           'mexican': ['mexico', 'mexican'],
                           'british': ['english', 'british', 'britan', 'england'],
                           'german': ['german', 'germany'],
                           'indian': ['indian', 'india'],
                           'indonesian': ['indonesia', 'indonesian', 'goreng', 'kecap', 'rendang', 'sumatra', 'sumatran'],
                           'cajun': ['cajun'],
                           'carribean': ['caribbean', 'cuba', 'jamaica', 'jamaican', 'cuban'],
                           'thai': ['thai', 'thailand'],
                           'vietnamese': ['vietnamese', 'vietnam', 'banh', ' pho '],
                           'irish': ['irish', 'ireland'], 
                           'korean': ['korea', 'korean', 'kalbi', 'bulgogi', 'bibimbap', 'kimchi'],
                           'japanese': ['japan', 'japanese', 'sake', 'miso', 'matcha', 'sushi'],
                           'chinese': ['china', 'chinese', 'cantonese', 'shanghai', 'dim sum', 'mongol', 'mongolian'],
                           'italy': ['italy', 'risotto', 'bruschetta', 'piccata', 'brisato', 'bucatini', 'bolognese',
                                     'parmagiana', 'tuscan', 'toscana']}
    
    def get_recipes(self, data_sets):
        for filename in data_sets:
            with open(filename, 'r') as f:
                all_recipes = json.load(f)
        cleaned_ar = self.clean_recipes(all_recipes)
        self.complete_countries(cleaned_ar)
        self.build_cookbook()
        
    def complete_countries(self, cleaned_ar):
        for r in range(len(cleaned_ar)-1):
            terms = cleaned_ar[r]
            for k, v in normal_terms.items():
                terms = terms.replace(k, v)
            cuisine = self.find_cuisine(terms)
            if cuisine != 'unk':
                if cuisine == 'italy':
                    cuisine = 'italian'
                self.countries[cuisine]['recipes'].append(terms)

    def clean_recipes(self, all_recipes):
        cleaned_ar = []
        for r in all_recipes:
            recipe = ''
            try:
                if 'title' in all_recipes[r]:
                    recipe += all_recipes[r]['title']
                if 'ingredients' in all_recipes[r]:
                    recipe += ", ".join(all_recipes[r]['ingredients'])
                if 'instructions' in all_recipes[r]:
                    recipe += all_recipes[r]['instructions']
                cleaned_ar.append(recipe.lower())
            except:
                continue
        return cleaned_ar
    
    def find_cuisine(self, recipe):
        for country in self.cuisine_id:
            if country in recipe:
                return country
            for word in self.cuisine_id[country]:
                if word in recipe:
                    return(country)
        return 'unk'
    
    def build_cookbook(self):
        for c in self.countries:
            for r in range(len(self.countries[c]['recipes'])-1):
                terms = self.countries[c]['recipes'][r]
                for k, v in normal_terms.items():
                    terms = terms.replace(k, v)
                self.cookbook['recipes'].append(terms)
                self.cookbook['cuisine'].append(c)