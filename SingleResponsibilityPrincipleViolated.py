class MLModel:

    def preprocess(self,data):
        print("Preprocessing the data...")
        return data

    def train(self,features):
        print("Model has been trained...")

    def evaluate(self):
        print("Model has been evaluated....")


if __name__ == "__main__":

    data = [1,2,3,4,5]
    model = MLModel()
    features = model.preprocess(data)
    model.train(features)
    model.evaluate()

