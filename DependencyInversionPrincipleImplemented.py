from abc import ABC, abstractmethod


class DataSource(ABC):

    def extract(self):
        pass


class AzureSynapseDS(DataSource):

    def extract(self):
        print("Extracting Data from Azure Synapse.....")


class AzureDataLakeDS(DataSource):

    def extract(self):
        print("Extracting Data from Azure DataLake....")


class DEPipeline:

    def __init__(self,datasource):
        self.datasource = datasource

    def extract(self):
        self.datasource.extract()


if __name__ == "__main__":

    data = [1,2,3]
    azure_synapse_ds = AzureSynapseDS()
    azure_datalake_ds = AzureDataLakeDS()

    de_pipeline_synapse = DEPipeline(azure_synapse_ds)
    de_pipeline_datalake = DEPipeline(azure_datalake_ds)
    de_pipeline_synapse.extract()
    de_pipeline_datalake.extract()