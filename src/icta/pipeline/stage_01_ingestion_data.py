from icta.components.ingestion_data import PrepareData
from pathlib import Path

class IngestionDataPipeLine:
    def __init__(self, path):
        self.path = path

    def main(self):
        prepare_data = PrepareData(path=self.path)
        prepare_data.load_data()
        data = prepare_data.feature_engineering()

STAGE_01 = "INGESTION DATA"

if __name__ == "__main__":
    print(f"<<<<<<<<<<<<<{STAGE_01} STARTED >>>>>>>>>>>>>>>")
    ingestion_data = IngestionDataPipeLine("datasets/final-customer.csv")
    ingestion_data.main()
    print(f"<<<<<<<<<<<<<{STAGE_01} STARTED >>>>>>>>>>>>>>>")