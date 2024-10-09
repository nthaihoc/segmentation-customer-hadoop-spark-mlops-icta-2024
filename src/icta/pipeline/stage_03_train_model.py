from icta.components.train_model import TrainingModel

class TrainingModelPipeLine:
    def __init__(self, session, path, file_path):
        self.session = session
        self.path = path
        self.file_path = file_path

    def main(self):
        training_model = TrainingModel(session=self.session,
                                       path=self.path,
                                       file_path=self.file_path)
        training_model.train_model()



