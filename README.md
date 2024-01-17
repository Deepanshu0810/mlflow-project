# mlflow-project
This is an end-to-end ML project which demonstrates the working of mlflow and ML in production

## Environment Setup
1. Create a virtual environment
    - `python -m venv env`
2. Activate the virtual environment
    - `source env/bin/activate`
3. Install the dependencies
    - `pip install -r requirements.txt`
4. Create the project structure
    - `python template.py`
5. Setup Tools
    - `python setup.py`

## Project Flow
1. Data Ingestion Pipeline
    - using the pipeline first create the artifacts folder and data ingestion folder in it
    - download the data from the source and store it in the data ingestion folder
    - unzip the data and store it in the folder
