from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, count

# Crear sesión de Spark

spark = SparkSession.builder \
    .appName("Batch Medicamentos Colombia") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Carga los datos

df = spark.read.csv("medicamentos.csv", header=True, inferSchema=True)

print("=== ESQUEMA DEL DATASET ===")
df.printSchema()

print("=== PRIMEROS REGISTROS ===")
df.show(5)

# Elimina valores nulos

df_clean = df.dropna()

df_clean = df_clean.withColumn("precio_por_tableta", col("precio_por_tableta").cast("double"))

# Exportacion de datos

print("=== PROMEDIO DE PRECIOS ===")
df_clean.select(avg("precio_por_tableta")).show()

print("=== PRECIO MAXIMO ===")
df_clean.select(max("precio_por_tableta")).show()

print("=== PRECIO MINIMO ===")
df_clean.select(min("precio_por_tableta")).show()

print("=== TOTAL DE REGISTROS ===")
df_clean.select(count("*")).show()

print("=== TOP 10 MEDICAMENTOS MAS COSTOSOS ===")
df_clean.orderBy(col("precio_por_tableta").desc()).show(10)

# Muestra los datos

print("=== PROMEDIO DE PRECIO POR MEDICAMENTO ===")
df_clean.groupBy("nombre_comercial") \
    .agg(avg("precio_por_tableta").alias("precio_promedio")) \
    .orderBy(col("precio_promedio").desc()) \
    .show(10)

# Fin

spark.stop()
