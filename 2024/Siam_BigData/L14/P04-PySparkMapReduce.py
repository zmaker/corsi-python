from pyspark import SparkContext

sc = SparkContext('local', 'MapReduceExample')

nomi = ['Rossi Mario 25', 'Bianchi Luigi 23','Verdi Giuseppe 18', 'Anna Blue 28']
rdd = sc.parallelize(nomi)
eta_min = rdd.map(lambda riga : int(riga[-2:])).min()
print("eta minima:", eta_min)

print(rdd.map(lambda riga : riga.split()) \
               .map(lambda x : (f"{x[1]} {x[0]}", int(x[2]))) \
               .sortBy(lambda tup : tup[1], ascending=False) \
      .collect())

numeri = [12,23,34,45,56,67,78,89,32,43,54,65,76,87,98]
rdd2 = sc.parallelize(numeri)
print(rdd2.map(lambda n : (('D' if (n%2) else 'P'), n)) \
      .reduceByKey(lambda a,b : a+b) \
      .collect())

sc.stop()