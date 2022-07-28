from etl.spark_etl import *


def main():
    spark = create_spark_session("myApp")
    
    path = "/location/to/file"
    options = {"header": True}
    sales_df = read_data(path, "csv", options, spark)
    
    items_count_df = get_items_count(sales_df)


if __name__ == "__main__":
    main()