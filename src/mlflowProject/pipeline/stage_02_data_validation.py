from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.data_validation import DataValidation
from mlflowProject import logger

PIPELINE_NAME = "Data Validation Pipeline"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
        pipeline = DataValidationPipeline()
        pipeline.main()
        logger.info(f">>>>> Completed Pipeline {PIPELINE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e