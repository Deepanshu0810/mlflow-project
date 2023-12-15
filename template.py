import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'mlflowProject'

# Create project directory
files = [
    './github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app,py',
    'requirements.txt',
    'setup.py',
    'research/test.ipynb',
    'templates/index.html',
]

for file in files:
    filePath = Path(file)
    filedir, filename = os.path.split(filePath)

    if filedir!='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory {filedir} for file: {filename}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
    
        with open(filePath, 'w') as f:
            pass
            logging.info(f"Created empty file: {filename}")

    else:
        logging.info(f"File already exists: {filename}")