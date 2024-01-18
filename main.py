from mlflowProject import logger
from mlflowProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlflowProject.pipeline.stage_02_data_validation import DataValidationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Starting Stage {STAGE_NAME} <<<<<")
    dataingestion = DataIngestionPipeline()
    dataingestion.main()
    logger.info(f">>>>> Completed Stage {STAGE_NAME} <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> Running Pipeline {STAGE_NAME} <<<<<")
    pipeline = DataValidationPipeline()
    pipeline.main()
    logger.info(f">>>>> Completed Pipeline {STAGE_NAME} <<<<<")
except Exception as e:
    logger.exception(e)
    raise e