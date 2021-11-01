from abc import ABC, abstractmethod

class MLAlgorithm(ABC):

    def fit_transform(self,data):
        pass

    def predict(self,data):
        pass


class KNearestNeighbor(MLAlgorithm):

    def fit_transform(self,data):
        print("Fit Transforming KNN Model....")

    def predict(self,data):
        print("Predicting From KNN Model....")


class SupportVectorMachine(MLAlgorithm):

    def fit_transform(self,data):
        print("Fit Transforming SVM Model....")

    def predict(self,data):
        print("Predicting From SVM Model....")


class PrincipalComponentAnalysis(MLAlgorithm):

    def fit_transform(self,data):
        print("Fit Transforming PCA Model....")

    def predict(self,data):
        raise Exception("PCA is not a predictive algorithm but a dimensionality reduction algorithm...")


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
    pca_model.predict(data)