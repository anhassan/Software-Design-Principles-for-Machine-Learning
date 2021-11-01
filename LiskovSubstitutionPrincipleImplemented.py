from abc import ABC, abstractmethod

class FeatureImputer(ABC):

    @abstractmethod
    def impute(self,data):
        pass


class CategoricalFeatureImputer(FeatureImputer):

    def impute(self,data):
        print("Imputed Categorical Data....")


class NumericalFeatureImputer(FeatureImputer):

    def __init__(self,impute_type):
        self.impute_type = impute_type

    def impute(self,data):
        print("Imputed Numerical Data with Impute Type : {}".format(self.impute_type))


if __name__ == "__main__":

    data = [1,2,3]
    categorical_imputer = CategoricalFeatureImputer()
    numerical_imputer = NumericalFeatureImputer("medain")

    categorical_imputer.impute(data)
    numerical_imputer.impute(data)