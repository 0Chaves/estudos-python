import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# 1. Carregar o dataset
df = pd.read_csv('heart_disease.csv')

print(df.head())
print(df.isnull().sum())

# 2. Definir a coluna alvo
target_col = 'Heart Disease Status'

# 3. Separar atributos (X) e alvo (y)
X = df.drop(columns=[target_col])
y = df[target_col]

# 4. Codificar o alvo
le = LabelEncoder()
y = le.fit_transform(y)

# 5. Identificar colunas numéricas e categóricas
num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = X.select_dtypes(include=['object', 'string', 'category']).columns.tolist()

# 6. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 7. Preencher valores ausentes nas colunas numéricas com a média do treino
num_fill_values = {}

for col in num_cols:
    media = X_train[col].mean()
    num_fill_values[col] = media
    X_train.loc[:, col] = X_train[col].fillna(media)
    X_test.loc[:, col] = X_test[col].fillna(media)

# 8. Preencher valores ausentes nas colunas categóricas com a moda do treino
cat_fill_values = {}

for col in cat_cols:
    moda = X_train[col].mode()[0]
    cat_fill_values[col] = moda
    X_train.loc[:, col] = X_train[col].fillna(moda)
    X_test.loc[:, col] = X_test[col].fillna(moda)

# 9. Aplicar OneHotEncoder nas colunas categóricas
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

X_train_cat = encoder.fit_transform(X_train[cat_cols])
X_test_cat = encoder.transform(X_test[cat_cols])

cat_feature_names = encoder.get_feature_names_out(cat_cols)

X_train_cat_df = pd.DataFrame(X_train_cat, columns=cat_feature_names, index=X_train.index)
X_test_cat_df = pd.DataFrame(X_test_cat, columns=cat_feature_names, index=X_test.index)

# 10. Juntar colunas numéricas com colunas categóricas codificadas
X_train_final = pd.concat([X_train[num_cols], X_train_cat_df], axis=1)
X_test_final = pd.concat([X_test[num_cols], X_test_cat_df], axis=1)

print("\nShape treino:", X_train_final.shape)
print("Shape teste:", X_test_final.shape)

# 11. Treinar o modelo
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_final, y_train)

# 12. Fazer previsões
y_pred = model.predict(X_test_final)

# 13. Avaliar o modelo
print("\nAcurácia:", accuracy_score(y_test, y_pred))
print("\nMatriz de confusão:")
print(confusion_matrix(y_test, y_pred))
print("\nRelatório de classificação:")
print(classification_report(y_test, y_pred))

