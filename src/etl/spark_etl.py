from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


def create_spark_session(app_name):
    return (
        SparkSession
            .builder
            .master("local[*]")
            .appName(app_name)
            .getOrCreate()
    )

def stop_spark_context(spark):
    spark.stop()

def read_data(input_path, format, options, spark):
    return (
        spark
            .read
            .format(format)
            .options(**options)
            .load(input_path)
    )

def get_items_count(df):
    df_with_count = (
	df
	  .groupBy('user_id')
	  .agg(sum('item_count')
	  .alias('total_item_count'))
    )
    return df_with_count
