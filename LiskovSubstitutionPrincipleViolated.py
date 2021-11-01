from abc import ABC, abstractmethod

class FeatureImputer(ABC):

    @abstractmethod
    def impute(self,data):
        pass


class CategoricalImputer(FeatureImputer):

    def impute(self,data):
        print("Imputed Categorical Data....")

class NumericalImputer(FeatureImputer):

    def impute(self,data,impute_type):
        print("Imputed Numerical Data with Impute Type : {}....".format(impute_type))


if __name__ == "__main__":

     data = [1,2,3]
     categorical_imputer = CategoricalImputer()
     numerical_imputer = NumericalImputer()
     categorical_imputer.impute(data)
     numerical_imputer.impute(data,"mean")