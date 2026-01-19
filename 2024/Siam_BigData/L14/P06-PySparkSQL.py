from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("load csv").getOrCreate()

df = spark.read.csv("persone.csv", sep=';', header=True, inferSchema=True)
df.show()
df.printSchema()
print("righe: ", df.count())

#da RDD a DataFrame
sc = spark.sparkContext
dati = [('Mario', 'Rossi', 25),('Luigi', 'Bianchi', 34),('Giuseppe', 'Verdi', 18)]
rdd = sc.parallelize(dati)
df2 = spark.createDataFrame(rdd, ['Nome','Cognome', 'eta'])
df2.show()

#filtro dati su RDD
df.filter(df['sesso'] == 'F').show()

print("\ngroupby")
df.groupBy('sesso').count().show()

spark.stop()