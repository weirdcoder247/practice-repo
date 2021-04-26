# import packages
from sklearn.linear_model import ElasticNet, ElasticNetCV, LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV,\
    RandomizedSearchCV
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB,\
    ComplementNB
from sklearn.metrics import precision_score, recall_score, roc_auc_score,\
    mean_squared_error, accuracy_score, confusion_matrix,\
    classification_report
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Create sample dataset inputs of Features and Target Variable
X, y = make_classification(n_samples=1000, n_features=4,
                           n_informative=2, n_redundant=0, random_state=0,
                           shuffle=False)

# Create Model Object
clf = RandomForestClassifier(max_depth=2, random_state=0)

# Fit the Model
clf.fit(X, y)

# Predict
clf.predict([[0, 0, 0, 0]])
