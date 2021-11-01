
class AzureSynapseDS:

    def extract(self):
        print("Extracting Data from Azure Synapse....")

class DEPipeline:

    def __init__(self):
        self.datasource = AzureSynapseDS()

    def extract(self):
        self.datasource.extract()


if __name__ == "__main__":

    data = [1,2,3]
    de_pipeline = DEPipeline()
    de_pipeline.extract()