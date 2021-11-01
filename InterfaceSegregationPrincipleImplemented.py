from abc import ABC, abstractmethod

class MLAlgorithmTransformer(ABC):

    def fit_transform(self,data):
        pass


class MLAlgorithmPredictor(ABC):

    def predict(self,data):
        pass


class KNearestNeighbor(MLAlgorithmTransformer,MLAlgorithmPredictor):

    def fit_transform(self,data):
        print("Fit Transforming KNN Model....")

    def predict(self,data):
        print("Predicting from KNN Model....")


class SupportVectorMachine(MLAlgorithmTransformer,MLAlgorithmPredictor):

    def fit_transform(self,data):
        print("Fit Transforming SVM Model....")

    def predict(self,data):
        print("Predicting from SVM Model....")


class PrincipalComponentAnalysis(MLAlgorithmTransformer):

    def fit_transform(self,data):
        print("Fit Transforming PCA Model....")


if __name__ == "__main__":

    data = [1,2,3,4,5]

    knn_model = KNearestNeighbor()
    knn_model.fit_transform(data)
    knn_model.predict(data)

    svm_model = SupportVectorMachine()
    svm_model.fit_transform(data)
    svm_model.predict(data)

    pca_model = PrincipalComponentAnalysis()
    pca_model.fit_transform(data)