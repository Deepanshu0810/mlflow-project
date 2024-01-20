import pandas as pd
from sklearn.model_selection import train_test_split
from mlflowProject import logger
from mlflowProject.entity.config_entity import DataTransformationConfig
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # different transformation techniques can be added
    def train_test_splitting(self):
        df = pd.read_csv(self.config.data_file)
        train, test = train_test_split(df, test_size=0.2, random_state=42)

        train_data_path = os.path.join(self.config.root_dir, 'train.csv')
        test_data_path = os.path.join(self.config.root_dir, 'test.csv')

        train.to_csv(train_data_path, index=False)
        test.to_csv(test_data_path, index=False)

        logger.info(f"train data shape {train.shape}")
        logger.info(f"test data shape {test.shape}")