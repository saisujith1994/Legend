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
sc=spark.sparkContext

def casting(i):
    return int(i)

rdd=sc.textFile('richards.txt')

rdd= rdd.flatMap(lambda x: x.split(' ')).map(casting).filter(lambda x: x %2==0).distinct().collect()

print(rdd)