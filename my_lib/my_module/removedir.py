from pyspark.sql import SparkSession, DataFrame

from my_module.utils import get_dbutils

def remove_dir_using_dbutils(directory_to_remove):
    get_dbutils().fs.rm(directory_to_remove, True)

def read_spark_table(table) -> DataFrame:
    spark = SparkSession.getActiveSession()
    df = spark.table(table)
    return df