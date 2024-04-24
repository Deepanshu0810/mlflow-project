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

2. Data Validation Pipeline
    - using the pipeline first create the artifacts folder and data validation folder in it
    - read the data from the data ingestion folder
    - validate the data and store the validation report in the data validation folder

3. Data Preprocessing Pipeline
    - using the pipeline first create the artifacts folder and data preprocessing folder in it
    - read the data from the data ingestion folder
    - preprocess the data and store it in the data preprocessing folder

4. Model Training Pipeline
    - using the pipeline first create the artifacts folder and model training folder in it
    - read the data from the data preprocessing folder
    - train the model and store it in the model training folder

