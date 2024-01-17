import os
import urllib.request as request
import zipfile
from mlflowProject import logger
from mlflowProject.utils.common import get_size
from mlflowProject.entity.config_entity import DataIngestionConifg
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConifg):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_url, self.config.local_data_file)
            logger.info(f"Downloaded {filename} with follwoing headers:\n{headers}")
        else:
            logger.info(f"File already exist of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)