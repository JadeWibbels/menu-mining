import numpy as np

class DietModel:
    def __init__(self, training, min_count):
        self.training = training
        self.min_count = min_count
        self.model = {}
        self.N = 0
        self.ingredients = {}
        self.vocab = 0
        
    def build_model(self):
        for item in self.training:
            if item['cuisine'] not in self.model:
                self.model[item['cuisine']] = {'ingredients':{},
                                               'N': 0,
                                               'vocab': 0,
                                               'count': 0,
                                               'avg_ingredient_count': 0}
            if self.model[item['cuisine']]['count'] >= self.min_count:
                continue
            for i in item['ingredients']:
                words = i.split()
                for w in words:
                    if w not in self.ingredients:
                        self.ingredients[w] = 1
                        self.vocab +=1
                    else:
                        self.ingredients[w] +=1
                    self.N +=1
                    if w not in self.model[item['cuisine']]['ingredients']:
                        self.model[item['cuisine']]['ingredients'][w] = 1
                        self.model[item['cuisine']]['vocab'] += 1
                    else:
                        self.model[item['cuisine']]['ingredients'][w] +=1
                    self.model[item['cuisine']]['N']+=1
            self.model[item['cuisine']]['count'] +=1
                    
    def clean_up(self):
        for region in self.model:
            clean = []
            for item in self.model[region]['ingredients']:
                if self.model[region]['ingredients'][item] <= 1:
                    clean.append(item)
            for item in clean:
                count = self.model[region]['ingredients'][item]
                del self.model[region]['ingredients'][item]
                self.model[region]['N'] -= count
                self.model[region]['vocab'] -=1
                self.N -= count
                
    def menu_classification(self, ingredients):
        r = {r:1 for r in self.model}
        r['world'] = -1
        for item in ingredients:
            for region in self.model.keys():
                if region == 'world':
                    continue
                else:
                    r[region] = self.get_region(item, r[region], region)
        max_prob = -100
        country = None
                
        for key, val in r.items():
            if val > max_prob:
                max_prob = val
                country = key
        print(country, max_prob)
        #for region in r:
        #    print(region, ": ", r[region])
    
    def get_region(self, item, val, region):
        if item in self.model[region]['ingredients']:
            new_value = val * ((self.model[region]['ingredients'][item] +.25) /
                              (self.model[region]['total_items'] + (self.model['world']['total_items'])))
            return new_value
        else:
            if item in self.model['world']['ingredients']:
                new_value = val * ((1)/(1+ (self.model['world']['total_items'])))
                return new_value
            else:
                return val