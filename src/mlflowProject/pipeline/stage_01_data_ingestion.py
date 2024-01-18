from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.data_ingestion import DataIngestion
from mlflowProject import logger

PIPELINE_NAME = "Data Ingestion Pipeline"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_file()
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(f">>>>> Completed Pipeline {PIPELINE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e