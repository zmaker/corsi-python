from pyspark import SparkContext

sc = SparkContext('local', 'PartitionExample')

numeri = range(0,20)
rdd = sc.parallelize(numeri)
n = rdd.getNumPartitions()
print("partizioni: ", n);
print(rdd.glom().collect())

rdd2 = sc.parallelize(numeri, 4)
n = rdd2.getNumPartitions()
print("partizioni: ", n);
print(rdd2.glom().collect())

rdd3 = rdd.map(lambda n : (n%5, n))
rdd4 = rdd3.partitionBy(5)
print(rdd4.glom().collect())

rdd5 = rdd4.coalesce(3)
print(rdd5.glom().collect())

rdd5.saveAsTextFile('rdd5')

sc.stop()