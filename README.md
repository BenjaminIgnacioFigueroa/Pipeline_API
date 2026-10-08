# ETL Pipeline: Procesamiento y Enriquecimiento de Posts

Un pipeline de datos robusto y modular construido en Python para la ingesta, limpieza, validación y exportación de publicaciones de usuarios. Este proyecto aplica estándares profesionales de ingeniería de datos, incluyendo tolerancia a fallos, testing automatizado y exportación multiformato.

## Objetivos del Proyecto
* **Extracción confiable:** Consumo de datos con mecanismos de reintento (`retries`) y manejo de tiempos de espera (`timeouts`) para asegurar la disponibilidad.
* **Calidad de datos:** Transformación estandarizada y aplicación de reglas de negocio estrictas para garantizar la integridad de la información antes de su exportación.
* **Trazabilidad:** Implementación de un sistema de *logging* detallado que audita cada fase del proceso, tiempos de ejecución y volumetría.
* **Desempeño:** Exportación optimizada a formatos columnares (`Parquet`) para análisis eficiente, además del formato tradicional (`CSV`).

## Stack Tecnológico
* **Lenguaje:** Python 3.11+
* **Procesamiento de datos:** `pandas`
* **Formatos de salida:** `pyarrow` (Parquet)
* **Testing Automatizado:** `pytest`
* **Peticiones HTTP:** `requests`

## Estructura del Proyecto

```text
pipeline_posts/
├── src/
│   ├── ingesta.py         # Módulo de extracción con manejo de errores
│   ├── limpieza.py        # Transformación, merge de dataframes y limpieza
│   ├── validacion.py      # Control de calidad y reglas de negocio
│   ├── exportar.py        # Generación de archivos CSV y Parquet
│   └── pipeline.py        # Script principal que orquesta el flujo completo
├── tests/
│   ├── test_limpieza.py   # Pruebas unitarias de las transformaciones
│   └── test_validacion.py # Pruebas unitarias de las reglas de calidad
├── output/                # Directorio de datos procesados (ignorado en git)
├── requirements.txt       # Dependencias fijadas para reproducibilidad exacta
└── README.md

Instalación y Configuración
Clonar el repositorio:

Bash
git clone [https://github.com/TU_USUARIO/pipeline_posts.git](https://github.com/TU_USUARIO/pipeline_posts.git)
cd pipeline_posts
Crear y activar un entorno virtual aislado:

Bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Mac/Linux
python -m venv venv
source venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Ejecución del Pipeline
Para correr el proceso completo, ejecuta el script principal desde la raíz del proyecto. El sistema generará logs en la consola detallando el progreso paso a paso de la extracción, transformación y carga:

Bash
python src/pipeline.py
(Nota Windows: si la consola arroja errores de visualización por caracteres especiales en los logs, ejecuta $env:PYTHONUTF8=1 antes del script para forzar UTF-8).

Testing
El proyecto incluye una suite de pruebas para prevenir regresiones y garantizar que la lógica central funcione como se espera. Para correr los tests:

Bash
python -m pytest tests/ -v
