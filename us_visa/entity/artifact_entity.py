from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Artifact class that holds the output of the data ingestion process.

    Attributes:
        trained_file_path (str): Path to the processed training dataset.
        test_file_path (str): Path to the processed test dataset.
    """
    trained_file_path: str
    test_file_path: str

    # # To perform additional setup after initialization.
    # def __post_init__(self):
    #     self.trained_file_path = self.trained_file_path
    #     self.test_file_path = self.test_file_path
        
        
        
        