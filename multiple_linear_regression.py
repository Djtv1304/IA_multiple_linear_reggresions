# Múltiple regresión lineal en Python

# Importación de las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # <— necesario para la matriz de correlación
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Cargar el dataset
dataset = pd.read_csv('f1_pitstops_2018_2024.csv')

# 2. Separar y = columna 'Laps' (índice 5)
y = dataset.iloc[:, 5].values

# 3. Crear X eliminando la columna de índice 5
X = dataset.drop(columns=dataset.columns[5])

# 4. Eliminar columnas no numéricas irrelevantes
X = X.drop(columns=['Date', 'Time_of_race', 'Pit_Time', 'Abbreviation', 'Race Name'], errors='ignore')

# ————————————————————————————————————————————————
# 5. Matriz de correlación de las variables numéricas seleccionadas
vars_corr = ['AvgPitStopTime', 'TotalPitStops', 'Wind_Speed_KMH', 'Air_Temp_C', 'Humidity_%', 'Laps']
df_corr = dataset[vars_corr]  # extraemos esas columnas directamente
plt.figure(figsize=(8,6))
sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación de Variables Seleccionadas')
plt.show()
# ————————————————————————————————————————————————

# 6. Columnas categóricas a codificar
cat_cols = ['Circuit', 'Driver', 'Constructor', 'Location', 'Country', 'Tire Compound']

# 7. One-Hot Encoding de las categóricas (el resto, passtrough)
ct = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(drop='first', sparse_output=False), cat_cols)],
    remainder='passthrough'
)
X_encoded = ct.fit_transform(X)

# 8. División en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=0
)

# 9. Entrenar el modelo de regresión lineal múltiple
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# 10. Predicciones
y_pred = regressor.predict(X_test)

# 11. Métricas de evaluación
mse = mean_squared_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)
print(f"MSE: {mse:.2f}")
print(f"R²:  {r2:.4f}")

# 12. Mostrar predicciones vs reales (dos decimales)
np.set_printoptions(precision=2)
resultados = np.concatenate([y_pred.reshape(-1,1), y_test.reshape(-1,1)], axis=1)
print("\nPredicción vs Real (Pred, Real):")
print(resultados)

# 13. Gráfico: valores reales vs predicciones
plt.figure(figsize=(10,6))
plt.scatter(range(len(y_test)), y_test, color='blue',  label='Valores reales')
plt.scatter(range(len(y_pred)), y_pred, color='red',   label='Predicciones')
plt.title('Predicciones vs Valores reales (Laps)')
plt.xlabel('Índice de muestra')
plt.ylabel('Vueltas completadas (Laps)')
plt.legend()
plt.grid(True)
plt.show()




