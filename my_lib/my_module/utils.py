def get_dbutils() -> None:
  """
  This is to make your local env happy :)
  """
  from pyspark.sql import SparkSession
  spark = SparkSession.getActiveSession()
  if spark.conf.get("spark.databricks.service.client.enabled") == "true":
    from pyspark.dbutils import DBUtils
    return DBUtils(spark)
  else:
    import IPython
    return IPython.get_ipython().user_ns["dbutils"]