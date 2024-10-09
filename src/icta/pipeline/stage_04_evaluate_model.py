from icta.components.evaluate_model import EvaluateModel

class EvaluateModelPipeLine:
    def __init__(self, session, path, file_path):
        self.session = session
        self.path = path
        self.file_path = file_path

    def main(self):
        evaluate_model = EvaluateModel(session=self.session,
                                       path=self.path,
                                       file_path=self.file_path)
        evaluate_model.plot_silhouette()
