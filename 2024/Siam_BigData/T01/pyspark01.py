from pyspark import SparkContext

# Crea un SparkContext
sc = SparkContext("local", "RDD_example")

# Crea una lista di numeri
lista_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crea un RDD dalla lista di numeri utilizzando il metodo parallelize
rdd_numeri = sc.parallelize(lista_numeri)

# Stampa il contenuto dell'RDD
print("Contenuto dell'RDD:")
print(rdd_numeri.collect())
print(rdd_numeri)
print("count", rdd_numeri.count())
print("somma", rdd_numeri.sum())
print("devstand", rdd_numeri.stdev())

#RDD da file
rdd2 = sc.textFile('numeri.txt')
print(rdd2)

print("count", rdd2.count())

# Chiudi il contesto Spark
sc.stop()