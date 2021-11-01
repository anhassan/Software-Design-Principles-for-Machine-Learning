from abc import ABC, abstractmethod

class FeatureExtractor(ABC):

    @abstractmethod
    def extract(self,data):
        pass

class CategoricalFeatureExtractor(FeatureExtractor):

    def extract(self,data):
        print("Extracted Categorical Features....")


class NumericalFeatureExtractor(FeatureExtractor):

    def extract(self,data):
        print("Extracted Numerical Features....")


class MLPipeline:

    def __init__(self,extractor):
        self.extractor = extractor

    def run(self,data):
        print("Running the Pipeline....")
        self._extract(data)

    def _extract(self,data):
        self.extractor.extract(data)


if __name__ == "__main__":

    data = [1,2,3]
    numerical_feature_extractor = NumericalFeatureExtractor()
    ml_pipeline = MLPipeline(numerical_feature_extractor)
    ml_pipeline.run(data)