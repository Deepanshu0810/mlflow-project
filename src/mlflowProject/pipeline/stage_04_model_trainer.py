from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.model_trainer import ModelTrainer
from mlflowProject import logger

PIPELINE_NAME = "Model Trainer Pipeline"

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_config = config.get_model_config()
            model_trainer = ModelTrainer(model_config)
            model_trainer.train()
        except Exception as e:
            logger.error(e)
            raise e
        
if __name__=="__main__":
    try:
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        logger.info(f">>>>> Running Pipeline {PIPELINE_NAME} <<<<<")
    except Exception as e:
        logger.error(e)
        raise e