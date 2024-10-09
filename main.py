from pyspark.sql import SparkSession
from icta.pipeline.stage_01_ingestion_data import IngestionDataPipeLine
from icta.pipeline.stage_02_spark_session import SparkSessionPipeLine
from icta.pipeline.stage_03_train_model import TrainingModelPipeLine
from icta.pipeline.stage_04_evaluate_model import EvaluateModelPipeLine


spark = SparkSession.builder.appName("Segmentation Customer").getOrCreate()

path_file_csv = "hdfs://localhost:9000/nthaihoc/data/rfm-customer.csv"
path_file_parquet = "hdfs://localhost:9000/nthaihoc/data/train-pyspark.parquet"
path_file_model = "artifacts/model"
path_file_result = "artifacts/results"

STAGE_02 = "SPARK SESSION"

print(f"<<<<<<<<<<<<<{STAGE_02} STARTED >>>>>>>>>>>>>>>")
spark_session = SparkSessionPipeLine(session=spark, 
                                     path=path_file_csv, 
                                     file_path=path_file_parquet)
spark_session.main()
print(f"<<<<<<<<<<<<<{STAGE_02} COMPLETED >>>>>>>>>>>>>>>")

STAGE_03 = "TRAINING MODEL"

print(f"<<<<<<<<<<<<<{STAGE_03} STARTED >>>>>>>>>>>>>>>")
train_model = TrainingModelPipeLine(session=spark,
                                    path=path_file_parquet,
                                    file_path=path_file_model)
train_model.main()
print(f"<<<<<<<<<<<<<{STAGE_03} COMPLETED >>>>>>>>>>>>>>>")

STAGE_04 = "EVALUATE MODEL"

print(f"<<<<<<<<<<<<<{STAGE_04} STARTED >>>>>>>>>>>>>>>")
evaluate_model = EvaluateModelPipeLine(session=spark,
                                       path=path_file_parquet,
                                       file_path=path_file_result)
evaluate_model.main()
print(f"<<<<<<<<<<<<<{STAGE_04} COMPLETED >>>>>>>>>>>>>>>")

spark.stop()