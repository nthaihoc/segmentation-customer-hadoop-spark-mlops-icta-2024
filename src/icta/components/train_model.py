from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
import json
from pyspark.sql import SparkSession
import os
class TrainingModel:
    def __init__ (self, session, path, file_path):
        self.session = session
        self.path = path
        self.file_path = file_path

    def train_model(self):
        self.data = self.session.read.parquet(self.path)
        self.data.show(5)
        metrics = ClusteringEvaluator(predictionCol="prediction",
                                      featuresCol="scaler_number",
                                      metricName="silhouette",
                                      distanceMeasure="squaredEuclidean")
        for i in range(2, 10):
            kmeans = KMeans(featuresCol="scaler_number",
                           k=i,
                           seed=42)
            model = kmeans.fit(self.data)
            model.save(os.path.join(self.file_path, f"model with k is {i}"))
        