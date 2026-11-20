from pyspark.sql import SparkSession
import os
import sys

python_path = sys.executable

os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

spark = (
    SparkSession.builder
    .master("local[2]")
    .appName("RDDLearning")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .getOrCreate()
)

sc = spark.sparkContext

#rdd=sc.textFile('richards.txt')

rdd=sc.textFile('quiz.txt')

rdd= rdd.flatMap(lambda x: x.split(' '))

def casting(x):
    return [int(i) for i in x]

def word_count(x):
    return [len(i) for i in x]

#rdd= rdd.map(casting)
#rdd=rdd.flatMap(casting)

rdd=rdd.filter(lambda x: x[0].lower()=='h' or x[0].lower()=='c')

print(rdd.collect())