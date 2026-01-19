from pyspark import SparkContext
# Crea un SparkContext
sc = SparkContext("local", "RDD_example")

rdd = sc.parallelize(range(1,25))
res = rdd.getNumPartitions()
print(res)

rdd = sc.parallelize(range(1,25), 4)
res = rdd.getNumPartitions()
print(res)

res = rdd.glom().collect()
print(res)

rdd2 = rdd.map(lambda x: (x%7, x)).partitionBy(6)
res = rdd2.glom().collect()
print(res)

rdd2.saveAsTextFile('rddsavefile')


# Chiudi il contesto Spark
sc.stop()

