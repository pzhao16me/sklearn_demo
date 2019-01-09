import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import cross_validition,metrics
from sklearn.grid_search import grid_searchCV
import matplotlib.pyplot as plt



# make and check the data

train = pd.read_csv("train_modified.csv")
target = 'Dishbured' # Dishbured 的值即为二元分类的输出
IDcol = "	ID"

# show the outputs of the labels
train["	Dishbured"].value_counts()

x_columns = [x for x in train.columns if x not in[target,IDcol]]
X = train[x_columns]
y = train['Dishbured']

# default parameters

gbm0 = GradientBoostingClassifier(random_seed=10)
gbm0.fit(X,y)
y_pred = gbm0.predict(X)
y_predprob = gbm0.predict_proba(X)[:,1]
print("Accuracy : %.4g " %,metrics.accuracy_score(y.values,y_pred))
print(" AUC Score (train):" % metrics.roc_auc_score(y,y_predprob))



#  tune the parameters
# 1 learnint_rate, n_estimators
param_test1 = {'n_estimators':range(20,80,10)}

gsearch1 = grid_searchCV(estimators = GradientBoostingClassifier(learnint_rate = 0.1,
																min_samples_split=300,
																min_samples_leaf =20,
																max_depth =8,
																max_features="sqrt",
																subsample=0.8,
																random_seed=10,
																param_grid =para_test1,
																scoring= 'roc_auc',
																iid=False,
																cv=5))
gsearch1.fit(X,y)
gsearch1.grid_scores_,gsearch1.best_params_,gsearch1.best_score_

# the best n_estimators will be :60

# 2  max_depth  and min_samples_split

param_test2 = {"max_depth": range(3,14,2),"min_samples_split":range(100,801,200)}



gsearch2 = grid_searchCV(estimators = GradientBoostingClassifier(learnint_rate = 0.1,
																n_estimators=60,
																min_samples_leaf =20,
																max_features="sqrt",
																subsample=0.8,
																random_seed=10,
																param_grid =param_test2,
																scoring= 'roc_auc',
																iid=False,
																cv=5))
gsearch2.fit(X,y)
gsearch2.grid_scores_,gsearch2.best_params_,gsearch2.best_score_



# 3 
param_test3 = {'min_samples_split':range(800,1900,200),'min_samples_leaf':(60,101,10)}
# 4
param_test4 = {'max_features':range(7,20,2)}

# 5
param_test5 = {'subsample':[0.6,.07,0.75,0.8,0.85,0.9]}