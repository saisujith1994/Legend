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

numbers = [10, 20, 30, 40, 50]

rdd = sc.parallelize(numbers)

print(rdd.collect())

spark.stop()