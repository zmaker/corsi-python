#RDD
'''
#se non va su win
#https://cwiki.apache.org/confluence/display/HADOOP2/WindowsProblems
#paolo.a — Oggi alle 10:49
#https://github.com/steveloughran/winutils/tree/master

import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
'''
from pyspark import SparkContext

sc = SparkContext("local", "Esempio RDD")

lista = [1,2,3,4,5,6,7,8,9,10]
rdd = sc.parallelize(lista)

print(rdd.collect())
print("operazioni base RDD")
print("sum()", rdd.sum())
print("max()", rdd.max())
print("min()", rdd.min())
print("count()", rdd.count())

print("stats()", rdd.stats())
print("stats().count()", rdd.stats().count())

def fuzzyval(n):
    if n < 3:
        print(f"{n} LOW")
    elif n < 6:
        print(f"{n} MID")
    else:
        print(f"{n} HI")
    
rdd.foreach(fuzzyval)

rdd.foreach(lambda x: print( f"({x}) HI" if x > 5 else f"({x}) LO"))

sc.stop()