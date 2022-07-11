from etl.spark_etl import *


def main():
    path = "/location/to/file"
    spark = create_spark_session("myApp")
    sales_df = read_data(path, "csv", spark)
    items_count_df = get_items_count(sales_df)


if __name__ == "__main__":
    main()