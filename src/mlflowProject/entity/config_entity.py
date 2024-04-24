from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConifg:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path
    data_file: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_file: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    training_data_file: Path
    testing_data_file: Path
    model: str
    alpha: float
    l1_ratio: float
    target_column: str