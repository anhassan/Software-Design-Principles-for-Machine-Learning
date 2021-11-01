class Preprocessor:

    def preprocess(self,data):
        print("Preprocessing the data...")
        return data


class MLModel:

    def train(self,features):
        print("Model has been trained...")
        return features


class Evaluator:

    def evaluate(self,model):
        print("Model has been evaluated...")


if __name__ == "__main__":

    data = [1,2,3]
    features = Preprocessor().preprocess(data)
    model = MLModel().train(features)
    Evaluator().evaluate(model)