import pytest
import pandas as pd
from etl import spark_etl


@pytest.fixture(scope="session")
def spark():
    return spark_etl.create_spark_session("testApp")

@pytest.fixture(scope="session")
def sales_df(spark):
    path = "./tests/data/sales_sample.csv"
    file_format = "csv"
    options = {"header": True}
    return spark_etl.read_data(path, file_format, options, spark)


class TestSparkETL:

    def test_load_csv(self, sales_df):
        actual = ["user_id", "tx_id", "item_name", "item_count", "timestamp"]
        expected = [field.name for field in sales_df.schema]
        
        assert expected == actual

    def test_get_items_count(self, sales_df):
        expected = {
            "user_id": ["1", "2", "3", "4"], 
            "total_item_count": [10.0, 6.0, 3.0, 1.0]
        }
        expected_df = pd.DataFrame(data=expected)

        actual_df = (
            spark_etl
                .get_items_count(sales_df)
                .orderBy("user_id")
                .toPandas()
        )

        assert expected_df.equals(actual_df) is True

