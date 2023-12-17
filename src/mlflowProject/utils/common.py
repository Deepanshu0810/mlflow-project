import os
from box.exceptions import BoxValueError
import yaml
from mlflowProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a yaml file and return a ConfigBox object"""
    try:
        with open(path_to_yaml, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"File loaded: {path_to_yaml}")
    except BoxValueError:
        raise ValueError(f"File is empty: {path_to_yaml}")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_dir: list, verbose=True):
    for path in path_to_dir:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Directory created: {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists: {path}")

@ensure_annotations
def save_json(path_to_file: Path, data: dict, verbose=True):
    joblib.dump(data, path_to_file)
    logger.info(f"File saved: {path_to_file}")

@ensure_annotations
def laod_bin(path_to_file: Path) -> Any:
    data = joblib.load(path_to_file)
    logger.info(f"File loaded: {path_to_file}")
    return data

@ensure_annotations
def get_size(path_to_file: Path) -> str:
    size = round(os.path.getsize(path_to_file)/1024)
    return f"~ {size} KB"