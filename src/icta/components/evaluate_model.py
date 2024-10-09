from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
import matplotlib.pyplot as plt
import os
import json
class EvaluateModel:
    def __init__(self, session, path, file_path):
        self.session = session
        self.path = path
        self.file_path = file_path
        self.data = self.session.read.parquet(self.path)
    def plot_silhouette(self):

        evaluator = ClusteringEvaluator(predictionCol="prediction",
                                       featuresCol="scaler_number",
                                       metricName="silhouette",
                                       distanceMeasure="squaredEuclidean")
        scores = []

        for i in range(2, 10):
            kmeans = KMeans(featuresCol='scaler_number', 
                            k=i, seed=42)
            model = kmeans.fit(self.data)
            predictions = model.transform(self.data)
            score = evaluator.evaluate(predictions)
            scores.append(score)

        self.save_json(os.path.join(self.file_path, "score.json"), score)

        plt.figure(figsize=(10, 6))
        plt.plot(range(2, 10), scores, marker='o')
        plt.title('Silhouette Scores for Different k')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Silhouette Score')
        plt.grid(True)
        plt.savefig(os.path.join(self.file_path, "Silhouette score of Kmeans for k cluster"))
        plt.show()

    @staticmethod
    def save_json(path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
