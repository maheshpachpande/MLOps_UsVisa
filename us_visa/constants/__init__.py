import os
from datetime import date

# ------------------------------
# ✅ MongoDB Constants
# ------------------------------
DATABASE_NAME = "us_visa"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL"

# ------------------------------
# ✅ General Project Constants
# ------------------------------
PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"
CURRENT_YEAR = date.today().year

# ------------------------------
# ✅ File Names
# ------------------------------
FILE_NAME = "usvisa.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
MODEL_FILE_NAME = "model.pkl"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# # ------------------------------
# # ✅ AWS Credentials & Config
# # ------------------------------
# AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
# AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
# REGION_NAME = "us-east-1"

# ------------------------------
# ✅ Data Ingestion Constants
# ------------------------------
DATA_INGESTION_COLLECTION_NAME = "visa_data"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

# # ------------------------------
# # ✅ Data Validation Constants
# # ------------------------------
# DATA_VALIDATION_DIR_NAME = "data_validation"
# DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
# DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"

# # ------------------------------
# # ✅ Data Transformation Constants
# # ------------------------------
# DATA_TRANSFORMATION_DIR_NAME = "data_transformation"
# DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
# DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"

# # ------------------------------
# # ✅ Model Trainer Constants
# # ------------------------------
# MODEL_TRAINER_DIR_NAME = "model_trainer"
# MODEL_TRAINER_TRAINED_MODEL_DIR = "trained_model"
# MODEL_TRAINER_TRAINED_MODEL_NAME = "model.pkl"
# MODEL_TRAINER_EXPECTED_SCORE = 0.6
# MODEL_TRAINER_MODEL_CONFIG_FILE_PATH = os.path.join("config", "model.yaml")

# # ------------------------------
# # ✅ Model Evaluation Constants
# # ------------------------------
# MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
# MODEL_BUCKET_NAME = "usvisa-model2024"
# MODEL_PUSHER_S3_KEY = "model-registry"

# # ------------------------------
# # ✅ FastAPI App Configuration
# # ------------------------------
# APP_HOST = "0.0.0.0"
# APP_PORT = 8080

# ------------------------------
# ✅ ML Constants
# ------------------------------
TARGET_COLUMN = "case_status"
