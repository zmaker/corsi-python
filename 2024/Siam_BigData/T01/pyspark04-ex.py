from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder \
    .appName("Caricamento_CSV") \
    .getOrCreate()

# Carica il file CSV escludendo l'intestazione
df = spark.read.csv("dati_vendite.csv", header=False)

# Stampa lo schema del DataFrame
df.printSchema()

# Mostra le prime righe del DataFrame
df.show()

print(df.count())

def f1(r):
    return (r[2], 1)

res = df.rdd.map(f1).countByKey()
print(res)

sc = spark.sparkContext
#dataframe da RDD
dati = [('Mario','Rossi', 123),('Mario','Verdi', 100),('Anna','Rossi', 99)]
rdd=sc.parallelize(dati)
df_da_rdd = spark.createDataFrame(rdd, ['n', 'c', 'imp'])
df_da_rdd.show()

df_da_rdd.registerTempTable('pers')
res=spark.sql('SELECT * FROM pers where imp < 100')

res.show()

# Chiudi la sessione Spark
spark.stop()



