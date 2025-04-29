# Predicción de Vueltas Completadas (Laps) en F1  
**Regresión Lineal Múltiple** con variables de pit stops y meteorología  

## 1. Contexto y Objetivo  
Se construyó un modelo de regresión lineal múltiple para **predecir el número de vueltas completadas** (`Laps`) por un piloto, usando como predictores:  
- `AvgPitStopTime`  
- `TotalPitStops`  
- `Wind_Speed_KMH`  
- `Air_Temp_C`  
- `Humidity_%`  

El dataset proviene de registros de pit stops de 2018 a 2024 y contiene más de 1000 muestras.

## 2. Matriz de Correlación  

![image](https://github.com/user-attachments/assets/5c0d71d4-16fd-485e-a039-3d3b73caabbc)

|                       | AvgPitStopTime | TotalPitStops | Wind_Speed_KMH | Air_Temp_C | Humidity_% | **Laps** |
|-----------------------|---------------:|--------------:|---------------:|-----------:|-----------:|---------:|
| **AvgPitStopTime**    |          1.00  |         0.28  |         –0.07  |     –0.06  |      0.08  |    0.02  |
| **TotalPitStops**     |          0.28  |         1.00  |          0.03  |     –0.05  |      0.03  |    0.29  |
| **Wind_Speed_KMH**    |         –0.07  |         0.03  |          1.00  |      0.30  |      0.30  |   –0.16  |
| **Air_Temp_C**        |         –0.06  |        –0.05  |          0.30  |      1.00  |      0.39  |   –0.09  |
| **Humidity_%**        |          0.08  |         0.03  |          0.30  |      0.39  |      1.00  |   –0.09  |
| **Laps**              |          0.02  |         0.29  |         –0.16  |     –0.09  |     –0.09  |    1.00  |

**Claves de interpretación**  
- La correlación máxima con `Laps` es **0.29** (`TotalPitStops`), moderada.  
- Los demás predictores tienen correlaciones lineales débiles (|ρ| < 0.16).  
- No hay colinealidad extrema (> 0.8) entre predictores.

## 3. Gráfico de Predicciones vs. Valores Reales  

![image](https://github.com/user-attachments/assets/fd314327-4de4-4aad-a10f-8d88421fc626)

- **Azul**: valores reales de `Laps`.  
- **Rojo**: predicciones del modelo.  

La **amplia dispersión** en torno al “banda central” (≈ 40–70 vueltas) muestra que, si bien hay tendencia general, existen predicciones atípicas (incluso negativas).

## 4. Métricas de Evaluación  

| Métrica        | Valor     | Interpretación                                                  |
|---------------:|----------:|-----------------------------------------------------------------|
| **MSE**        |    29.57  | Error cuadrático medio                                         |
| **RMSE**       | ≈ 5.44    |  \(\sqrt{29.57}\). Desviación promedio: ± 5.4 vueltas          |
| **R²**         |   0.8346  | Explica el 83.46 % de la varianza en `Laps`                     |

### 4.1. Interpretación de MSE / RMSE  
- Un **RMSE ≈ 5.4 vueltas** significa que, en promedio, las predicciones se desvían en 5–6 vueltas del valor real.  
- Dado un rango típico de 60–70 vueltas por carrera, este error es moderado (~ 8–9 %).

### 4.2. Interpretación de R²  
- Un **R² = 0.8346** indica que el **83.46 %** de la variabilidad de `Laps` está explicado por las cinco variables.  
- En contextos de regresión múltiple, un R² > 0.8 se considera **buen ajuste**, señal de que el modelo capta la señal principal.

## 5. Conclusiones y Recomendaciones

1. **Rendimiento actual**  
   - El modelo ofrece un **buen poder explicativo** (R² alto) pero con un **error práctico** (RMSE ≈ 5.4 vueltas) que debe valorarse según la aplicación.  
   - La dispersión de predicciones sugiere la presencia de outliers y casos extremos.

2. **Posibles mejoras**  
   - **Agregar variables** clave:  
     - Indicadores de interrupción (banderas rojas),  
     - Incidentes o penalizaciones,  
     - Tiempo total de carrera.  
   - **Modelos no lineales** (árboles, ensamblados) para capturar interacciones complejas.  
   - **Transformaciones** o límites (p.ej. predecir log(Laps), usar regresión con rango ≥ 0).  
   - **Validación cruzada** y análisis de residuos (homocedasticidad, normalidad).

3. **Uso práctico**  
   - Un RMSE de 5 vueltas puede ser aceptable para **simulaciones de estrategia**, pero insuficiente para **toma de decisiones milimétricas**.  
   - El alto R² permite tener **confianza** en la señal global del modelo.

---

> __Autor:__ Diego Toscano  
> __Contacto__: diego.toscano@udla.edu.ec
