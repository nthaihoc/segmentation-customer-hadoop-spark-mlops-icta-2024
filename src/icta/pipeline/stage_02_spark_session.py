from icta.components.spark_session import Spark

class SparkSessionPipeLine:
    def __init__(self, session, path, file_path):
        self.session = session
        self.path = path
        self.file_path = file_path

    def main(self):
        spark_session = Spark(session=self.session,
                              path=self.path,
                              file_path=self.file_path)
        spark_session.pyspark_transform()
