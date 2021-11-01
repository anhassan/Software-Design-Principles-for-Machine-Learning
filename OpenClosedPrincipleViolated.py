class FeatureExtractor:

    def extract_categorical_features(self,data):
        print("Extracted Categorical Features....")

    def extract_numerical_features(self,data):
        print("Extracted Numerical Features....")


class MLPipeline:

    def __init__(self,extractor,feature_type):
        self.extractor = extractor
        self.feature_type = feature_type

    def run(self,data):
        print("Running the Pipeline")
        features = self._extract(data)

    def _extract(self,data):

        if self.feature_type == "categorical":
            self.extractor.extract_categorical_features(data)
        elif self.feature_type == "numerical":
            self.extractor.extract_numerical_features(data)


if __name__ == "__main__":

    data = [1,2,3]
    feature_extractor = FeatureExtractor()
    ml_pipeline = MLPipeline(feature_extractor,"numerical")
    ml_pipeline.run(data)

