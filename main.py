from mlflowProject import logger
from mlflowProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Starting Stage {STAGE_NAME} <<<<<")
    dataingestion = DataIngestionPipeline()
    dataingestion.main()
    logger.info(f">>>>> Completed Stage {STAGE_NAME} <<<<<")
except Exception as e:
    logger.exception(e)
    raise e