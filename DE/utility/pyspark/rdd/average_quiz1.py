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

rdd= sc.textFile('average_quiz_sample.csv')

rdd= rdd.map(lambda x: x.split(','))

rdd_city= rdd.map(lambda x: (x[1],(float(x[2]),1)))

rdd_month= rdd.map(lambda x: (x[0],(float(x[2]),1)))

rdd_avg_city= rdd_city.reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))

rdd_avg_month = rdd_month.reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))

rdd_avg_city=rdd_avg_city.map(lambda x: (x[0],x[1][0]/x[1][1]))

rdd_avg_month=rdd_avg_month.map(lambda x: (x[0],x[1][0]/x[1][1]))

print(rdd_avg_city.collect(),'\n',rdd_avg_month.collect())