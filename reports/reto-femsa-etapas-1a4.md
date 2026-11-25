# Reto FEMSA · Etapas 1 a 4 · A01572331

**Jessica Lizeth Salazar Muñoz** · Soporte analítico para la toma de decisiones (TI2006B) · Grupo 303 · Equipo 5
Socio formador: **FEMSA, Auditoría Interna (vertical Financiera)**

## El reto
Auditoría Interna revisa por muestreo los registros de diario de Coca-Cola FEMSA (KOF). El objetivo es evaluar el **100% de los documentos contables** y señalar los que combinan cuentas de forma incompatible con el principio de devengación (NIIF) o con el flujo normal de la transacción, con reglas que Auditoría pueda cambiar sin tocar el código.

## Contenido
| Archivo | Qué es |
|---|---|
| [`notebooks/04-reto-femsa-etapas-1a4.ipynb`](../notebooks/04-reto-femsa-etapas-1a4.ipynb) | Notebook ejecutado con las cuatro etapas: entendimiento, exploración, limpieza en SQL con modelo dimensional, y análisis con reglas parametrizables |
| [`reports/Reporte_Ejecutivo_Reto_FEMSA_Jessica_Salazar.pptx`](Reporte_Ejecutivo_Reto_FEMSA_Jessica_Salazar.pptx) | Presentación ejecutiva de la evidencia |

## Cómo correrlo
1. Coloca `AnalisisDeRegistros_Datos.xlsx` (archivo del socio, no se versiona) en `data/raw/` (está en `.gitignore`), o súbelo en Colab con `files.upload()`.
2. Ejecuta todas las celdas. Requiere `pandas`, `openpyxl` y `matplotlib`; SQLite viene con Python.
3. Para cambiar el periodo de corte o el rezago máximo, edita la tabla `parametros`. Para agregar o desactivar una regla, edita `dim_regla`.

## Pipeline
`Excel del socio → pandas (ingesta y perfilamiento) → SQLite (correcciones y modelo) → tabla de reglas → excepciones y señales de control`

## Modelo dimensional lógico
Constelación con tres tablas de hechos:
- **Fact_Partida** (una fila por partida) · **Fact_Documento** (una por documento, unidad de análisis) · **Fact_Excepcion** (documento × regla)
- Dimensiones: Fecha (rol contable y creación), Sociedad/País, Usuario, Tipo de documento, Cuenta (con grupo de análisis) y **Regla** (parametrizable)

## Hallazgos principales
- Documentos evaluados: **84,893 (100%)**, $5,087.5 M en debe, 4 sociedades, enero a septiembre de 2026.
- Las cinco reglas del socio tal cual marcan **22,308** documentos; el 80% son facturas de venta normales con IVA (falso positivo de la regla Pasivos vs Ingresos).
- Con la exclusión parametrizada quedan **4,449 documentos por revisar (5.24%, $76.9 M)**. La captura manual es el 12% de ellos y el **80% del monto**.
- **624** documentos con señal de control: usuario dado de baja, usuario genérico, captura manual en fin de semana o creación posterior al corte.

## Siguientes pasos
Dashboard en Power BI (Etapa 5), validación de reglas de negocio con Auditoría, y conciliación contra balanzas cuando el socio las entregue.
