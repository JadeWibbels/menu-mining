import nltk

class Recipe:
    def __init__(self, uid, r):
        self.measures = ['bunch', 'block', 'cup', 'cups', 'pinch', 'tablespoon', 'tablespoons', 'ounces', 'ounce', 'oz',
                         'teaspoon', 'teaspoons', 'tsp', 'pound', 'pounds', 'sheets', 'slice', 'wheel', 'bag', 'bags',
                         'gram', 'grams', 'sticks', 'ml', 'mL', 'kg', 'milliliter', 'liter', 'L', 'package', 'packages',
                         'can', 'cans']
        self.raw = r
        self.uid = uid
        self.shopping_list = []
        self.instructions = r['instructions'].lower().replace('adverstisement', '')
        self.ingredients = {}
        if 'title' in r:
            self.title = r['title'].split()
            
    # strip and lower

    def ingredients_list(self):
        for entry in self.raw['ingredients']:
            clean_entry = entry.replace('-', ' ').replace('/', ' ').lower().replace('advertisement', '')
            tokens = nltk.word_tokenize(clean_entry)
            pos = nltk.pos_tag(tokens)
            #print(pos)
            unit = [x[0] for x in pos if x in self.measures]
            qty = [x[0] for x in pos if x[1] == 'CD' or x[1] == 'NNP']
            item = [x[0] for x in pos if x[1] == 'NN' and x[0] not in self.measures or x[1] =='NNS' and x[0] not in self.measures]
            notes = [x for x in tokens if x not in qty and x not in item]
            for i in item:
                self.ingredients[i]={'qty': ' '.join(qty), 'notes': ' '.join(notes)}
            self.shopping_list.append(' '.join(item))
            
            