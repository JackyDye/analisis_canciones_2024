# Análisis de Canciones 2024 - Spotify

Análisis exploratorio de datos (EDA) sobre canciones de Spotify con el objetivo de detectar principalmente patrones de éxito y el impacto de la viralidad de canciones en redes sociales sobre plataformas de streaming. Incluye limpieza del dataset, visualizaciones y un dashboard interactivo en Power BI.

---

## Estructura del repositorio

```
analisis_canciones_2024/
│
├── spotify_analysis.ipynb   # Notebook principal con EDA y visualizaciones
├── spotify_clean.csv        # Dataset limpio listo para análisis
└── Dashboard.pbix           # Dashboard interactivo en Power BI
```

---

## 🔍 ¿Qué contiene este proyecto?

### 1. Limpieza de datos (`spotify_clean.csv`)
- Eliminación de valores nulos y duplicados
- Normalización de columnas
- Cambio de tipo de datos
- Exportación del dataset limpio para su uso en el análisis y el dashboard

### 2. Análisis exploratorio (EDA)
- Correlación multiplataforma
- Modelos de éxito en base a patrones en los datos
- Impacto de redes sociales en Spotify
- Dominancia de canciones según su fecha de lanzamiento

### 3. Visualizaciones
- Gráficos de distribución de streams y repertorio
- Rankings de artistas y canciones más populares
- Comparativas y tendencias a lo largo del dataset

### 4. Dashboard en Power BI (`Dashboard.pbix`)
- Vista interactiva de los indicadores y gráficos

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Uso |
|---|---|
| SQL | Recolección de datos a través de base de datos local |
| Python | Limpieza, análisis y visualización |
| Pandas | Manipulación del dataset |
| Matplotlib / Seaborn | Gráficos exploratorios |
| Jupyter Notebook | Entorno de desarrollo |
| Power BI | Dashboard interactivo |

---

## Cómo ejecutar el proyecto

Para poder ejecutar el 100% del proyecto, es necesario tener el dataset. En mi caso, esos datos los subí a una base de datos local en SQL y luego me conecté a ella desde Python.

---

## Creditos

https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024

## 👤 Autor

**JackyDye**  
[GitHub](https://github.com/JackyDye)
