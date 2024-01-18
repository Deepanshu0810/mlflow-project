from mlflowProject.entity.config_entity import DataValidationConfig
import pandas as pd
from mlflowProject import logger


class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validate_status = None

            df = pd.read_csv(self.config.data_file)
            all_columns = list(df.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validate_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f'Validation Status: {validate_status}')
                    break
                    
                else:
                    validate_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f'Validation Status: {validate_status}')

            return validate_status
        
        except Exception as e:
            logger.error(e)
            raise e