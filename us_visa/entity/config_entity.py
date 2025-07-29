import os
from dataclasses import dataclass
from dotenv import load_dotenv
from us_visa.constants import *  # Load project-wide constants
from datetime import datetime

# -----------------------------
# ✅ Load environment variables from .env
# -----------------------------
load_dotenv()


# -----------------------------
# ✅ Training Pipeline Configuration
# -----------------------------
@dataclass
class TrainingPipelineConfig:
    # Name of the pipeline for training
    pipeline_name: str = PIPELINE_NAME
    
    # Directory to store artifacts
    artifact_dir: str = ARTIFACT_DIR


# Create an instance once so it can be reused by other configs
training_pipeline_config = TrainingPipelineConfig()


# -----------------------------
# ✅ Data Ingestion Configuration
# -----------------------------
@dataclass
class DataIngestionConfig:
    """
    Holds all paths and parameters required for data ingestion.
    """
    
    # Where the data will be downloaded
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    
    # Where the data wiill be stored
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME
    )
    
    # Where the train and test data will be stored
    training_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME
    )    
    testing_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME
    )
    
    # Split ratio of the data into train and test
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    
    # Name of the collection for MongoDB
    collection_name: str = DATA_INGESTION_COLLECTION_NAME
