# import the relevant parts of magpy
from magpy import core as c
from magpy import parse as p
# import general useful packages
import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
# import functions from scikit-learn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, roc_curve, auc, precision_recall_fscore_support
from sklearn.svm import SVC
import xgboost as xgb



# PARAMETERS
# the chosen embedding file (representation of atomic data in normalised vector form)
embed_f = r"C:\Users\tgp27\magpy\notebooks\cgcnn_embedding.json"

# get the material bandgap data
mat_f = r"C:\Users\tgp27\magpy\notebooks\bandgap-example.csv"
mat_df = pd.read_csv(mat_f)
# remove duplicate values - take the mean of bandgap values for each material
mat_df = mat_df.groupby('composition',as_index=False).mean()

# get material names as a list of strings
materials = mat_df['composition'].apply(''.join)
# get bandgaps as a list of floats
bandgaps = list(mat_df["Eg (eV)"])

# make a semiconductor flag - 0 if bandgap is zero, 1 if non zero
semicond = [1  if bandgaps[x] != 0 else 0 for x in range(len(bandgaps))]
y_clf = semicond

# FEATURE EXTRACTION
# get features for each material based on the weighted mean and std of the atomic values
# weights are simply stoichiometric weightings (see core.py for more info)
mat_features = c.descriptors(materials, embed_f, operations=["wmean","wstd"])

# MODEL TRAINING
# MODEL 1 FIRST, classifier to identify zero-bandgap materials (conductors)
# copied from example, SVC model
# we will use this for the test data, but for training we already know which materials have nonzero bandgap

# Split data into training and test sets (80:20)
X_train_clf = mat_features
#print(len(X_train_clf))
y_train_clf = semicond

# # Scale the input features to improve
scaler = StandardScaler().fit(X_train_clf)
X_train_clf = scaler.transform(X_train_clf)

# Define and fit the model
clf = SVC(probability=True, gamma='scale').fit(X_train_clf, y_train_clf)

# Make predictions on the test set
y_pred_clf = clf.predict(X_train_clf)



# MODEL 2 - predict bandgap from features

# only select data with nonzero bandgap
bandgap_filt = [bandgap for bandgap in bandgaps if bandgap != 0 ]
mat_fea_filt = [fea for bg,fea in zip(bandgaps,mat_features) if  bg != 0  ]

# Split data into training and test sets (90:10)
X_train, X_test, y_train, y_test = train_test_split(mat_fea_filt,bandgap_filt, test_size=0.2)

# convert to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)
dtrain = np.column_stack((X_train,y_train))

X_test = np.array(X_test)
y_test = np.array(y_test)
dtest = np.column_stack((X_test,y_test))

# read in data
dtrain = xgb.DMatrix(X_train,label=y_train)
dtest = xgb.DMatrix(X_test,label=y_test)
# specify parameters  - see xgboost online to find out what these mean.
param = {'max_depth':6, 'eta':0.3, 'gamma':1, 'silent':1 }
num_round = 100

# track progress
progress = dict()
watchlist  = [(dtrain,'train-rmse'), (dtest, 'eval-rmse')]

bst = xgb.train(param, dtrain, num_round, watchlist, evals_result=progress)
# make prediction
preds = bst.predict(dtest)

# print(progress)
# plot real test solutions versus training data
plt.scatter(y_test,preds)
plt.show()
