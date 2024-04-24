import pandas as pd
from mlflowProject import logger
from sklearn.linear_model import ElasticNet
from mlflowProject.entity.config_entity import ModelTrainerConfig
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def train(self):
        logger.info("Training model...")
        train = pd.read_csv(self.config.training_data_file)
        test = pd.read_csv(self.config.testing_data_file)
        X_train = train.drop([self.config.target_column], axis=1)
        X_test = test.drop([self.config.target_column], axis=1)
        y_train = train[self.config.target_column]
        y_test = test[self.config.target_column]

        lr = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        lr.fit(X_train, y_train)

        joblib.dump(lr, self.config.model)

        logger.info(f"Model trained and saved")