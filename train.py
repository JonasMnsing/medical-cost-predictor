import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor

# Parameters
max_depth = 10
n_estimators = 200
output_file = 'model.bin'

# Loading Data
df = pd.read_csv('insurance.csv')

# Splitting the data (combine train and val into full_train for the final model)
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1, stratify=df['smoker'])
df_full_train = df_full_train.reset_index(drop=True)

# Target variable
y_full_train = np.log1p(df_full_train.charges.values)
del df_full_train['charges']

# Feature extraction
dicts_full_train = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_full_train)

# Model training
model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=1)
model.fit(X_full_train, y_full_train)

# Save the model and DictVectorizer
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f"Model saved to {output_file}")