from pyspark import SparkContext
# Crea un SparkContext
sc = SparkContext("local", "RDD_example")

# Crea una lista di numeri
voti = [6,8,8,9,5,6,6,8]
# Crea un RDD dalla lista di numeri utilizzando il metodo parallelize
rdd_voti = sc.parallelize(voti)

res = rdd_voti.groupBy(lambda v: 'SUF' if v>=6 else 'INSUF') \
                        .mapValues(list) \
                        .collect()
print(res)

# Chiudi il contesto Spark
sc.stop()
