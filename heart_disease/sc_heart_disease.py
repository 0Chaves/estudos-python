import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


random_state = 66


df = pd.read_csv('heart_disease.csv')

print(df.head())
df.info()
df.describe()

# Verificar se há valores ausentes
print(df.isnull().sum())


# Separar os dados numéricos e os categóricos para posteriormente transformar os dados categóricos em números e facilitar o uso do algorítmo
df_categorical = df.select_dtypes(include=['str', 'object'])
df_numerical = df.select_dtypes(include=['int64', 'float64'])


# Transforma valores de string para dados numericos para que o algoritmo possa trabalhar
# Normalizar os dados e juntar num novo dataframe normalizado
le = LabelEncoder()
df_categorical_encoded = df_categorical.apply(le.fit_transform)

scaler = StandardScaler()
df_numerical_scaled = scaler.fit_transform(df_numerical)

df_processed = pd.concat([pd.DataFrame(df_numerical_scaled, columns=df_numerical.columns), df_categorical_encoded], axis=1)


# # Dividir os dados em features e target
X = df_processed.drop('Heart Disease Status', axis=1) # axis=1 é coluna, axis=0 é linha
y = df_processed['Heart Disease Status']

# # Dividir os dados em conjuntos de teino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

# # Treinar um modelo de classificação

from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier

model = RandomForestClassifier(random_state=random_state)

model.fit(X_train, y_train)

# # Avaliar o modelo
from sklearn.metrics import classification_report, confusion_matrix

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
