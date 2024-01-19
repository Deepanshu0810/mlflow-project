from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.data_transformation import DataTransformation
from mlflowProject import logger

PIPELINE_NAME = "Data Transformation Pipeline"

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.train_test_splitting()

if __name__=="__main__":
    try:
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e