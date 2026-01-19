from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("load csv").getOrCreate()

df = spark.read.csv("persone.csv", sep=';', header=True, inferSchema=True)
df.registerTempTable('pers')

res = spark.sql("SELECT * FROM pers WHERE sesso = 'F' ORDER BY peso")
res.show()

res2 = spark.sql("SELECT sesso, COUNT(*) FROM pers GROUP BY sesso")
res2.show()

#leggi e scrivi file parquet
df = spark.read.parquet()
spark.write.parquet()


spark.stop()
