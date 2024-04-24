from mlflowProject.constants import *
from mlflowProject.utils.common import read_yaml, create_directories
from mlflowProject.entity.config_entity import DataIngestionConifg, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            param_filepath =  PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(param_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConifg:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConifg(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            status_file = config.status_file,
            data_file = config.data_file,
            all_schema = schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_file = config.data_file,
        )

        return data_transformation_config
    
    def get_model_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params
        schema = self.schema

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            training_data_file = config.training_data_file,
            testing_data_file = config.testing_data_file,
            model = config.model,
            alpha = params.ElasticNet.alpha,
            l1_ratio = params.ElasticNet.l1_ratio,
            target_column = schema.TARGET.name
        )

        return model_trainer_config