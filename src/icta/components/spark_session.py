from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler

class Spark:
    def __init__(self, session, path, file_path):
        self.session = session
        self.path = path
        self.file_path = file_path

    def pyspark_transform(self):

        self.psdf = self.session.read.options(header=True, inferSchema=True).csv(self.path)
        col_number = self.psdf.columns
        num_vector = VectorAssembler(inputCols=col_number,
                                     outputCol="num_vector")
        
        train = num_vector.transform(self.psdf)

        scaler = StandardScaler(inputCol="num_vector",
                                outputCol="scaler_number",
                                withMean=True,
                                withStd=True)
        scaler_model = scaler.fit(train)
        train = scaler_model.transform(train)

        train.write.parquet(self.file_path)

        return train