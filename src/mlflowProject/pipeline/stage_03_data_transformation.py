from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.data_transformation import DataTransformation
from mlflowProject import logger
from pathlib import Path

PIPELINE_NAME = "Data Transformation Pipeline"

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]
            if status=="True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Data Schema is not valid")
            
        except Exception as e:
            logger.exception(e)
            raise e

if __name__=="__main__":
    try:
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e