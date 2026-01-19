# Importa le librerie necessarie
from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder \
    .appName("Import_CSV_Example") \
    .getOrCreate()

# Carica il file CSV in un DataFrame
#df = spark.read.csv("path/al/tuo/file.csv", header=True, inferSchema=True)
#lettura csv
df=spark.read.csv('persone.csv', sep=';', inferSchema=True, header=True)

# Mostra lo schema del DataFrame
print("Schema del DataFrame:")
df.printSchema()

# Mostra le prime righe del DataFrame
print("Primi 5 record del DataFrame:")
df.show(5)
df.describe().show()

# Esegui altre operazioni su df...

# Chiudi la sessione Spark
spark.stop()
