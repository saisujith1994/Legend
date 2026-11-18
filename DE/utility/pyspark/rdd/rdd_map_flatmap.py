from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[2]")
    .appName("RDDLearning")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .getOrCreate()
)

sc = spark.sparkContext

rdd=sc.textFile('richards.txt')

#rdd=sc.textFile('quiz.txt')

rdd= rdd.map(lambda x: x.split(' '))

def casting(x):
    return [int(i) for i in x]

def word_count(x):
    return [len(i) for i in x]

#rdd= rdd.map(casting)
rdd=rdd.flatMap(casting)

print(rdd.collect())