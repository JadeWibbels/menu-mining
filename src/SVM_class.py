import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import confusion_matrix, roc_auc_score, recall_score, precision_score

import numpy as np
parameters = {
    'clf__kernel':['rbf', 'linear'],
    'clf__gamma': np.logspace(-2.25, -1, 4),
    'clf__C': np.logspace(.6, .9, 4),
    'clf__degree':[1, 2, 3, 4]
}
print(parameters)

def tokenize(ingredients): 
    tknzr = TweetTokenizer()
    return tknzr.tokenize(ingredients)

en_stopwords = set(stopwords.words("english")) 

vectorizer = CountVectorizer( tokenizer= tokenize, min_df = 20)
vectorizer.fit_transform(X_train, y_train)


# split dataset using StratifiedKFold into 5 splits using sklearn.model_selection.StratifiedKFold.

skf = StratifiedKFold(n_splits=5, shuffle=False, random_state=None)
splits = skf.get_n_splits(X_train, y_train)

np.random.seed(1234)

pipeline = Pipeline([
    ('vect', vectorizer),
    ('clf', SVC()),
])

estimator = sorted(pipeline.get_params().keys()) 
print(estimator)

# Create GridSearchCV with pipeline and grid search parameters, scoring as accuracy.
grid_svm = GridSearchCV(pipeline, cv = splits, param_grid=parameters, scoring='accuracy', verbose=10)
grid_svm.fit(X_train, y_train)

print("best params:")
print(grid_svm.best_params_)

print("best cv score:")
print(grid_svm.best_score_)

def report_results(model, X, y):
    pred = model.predict(X)        
    acc = accuracy_score(y, pred)
    f1 = f1_score(y, pred)
    prec = precision_score(y, pred)
    rec = recall_score(y, pred)
    result = {'f1': f1, 'acc': acc, 'precision': prec, 'recall': rec}
    return acc
    
report_results(grid_svm.best_estimator_, X_test, y_test)