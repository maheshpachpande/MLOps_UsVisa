# =============================================
# ✅ Imports
# =============================================
import os
import sys
import pymongo
import certifi
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY

from dotenv import load_dotenv

# -----------------------------
# ✅ Load environment variables from .env
# -----------------------------
load_dotenv()

# =============================================
# ✅ Certificate Authority Path for TLS
# =============================================
ca = certifi.where()
# =============================================
# ✅ MongoDB Client Class
# =============================================
class MongoDBClient:
    """
    MongoDBClient is a singleton-style wrapper that connects to a MongoDB database using the URI
    from environment variables and handles connection with secure TLS.

    Attributes:
        client (pymongo.MongoClient): Shared MongoDB client object.
        database (pymongo.database.Database): Specific MongoDB database instance.
    """

    client = None  # Class-level shared MongoDB client

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            # -----------------------------
            # 🔄 Initialize MongoDB Client (once)
            # -----------------------------
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("MONGODB_URL_KEY")
                if not mongo_db_url:
                    raise ValueError(f"Environment variable is not set.")
                
                # Secure TLS connection using certifi bundle
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
                logging.info("✅ MongoDB client initialized successfully.")

            # -----------------------------
            # 📦 Set instance database
            # -----------------------------
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

            logging.info(f"✅ Connected to MongoDB database: {database_name}")

        except Exception as e:
            raise USvisaException(e, sys)


if __name__=="__main__":
    MongoDBClient()