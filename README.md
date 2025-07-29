# MLOps_UsVisa
- A comprehensive MLOps pipeline that automates model training, validation, deployment, and monitoring with CI/CD integration, feature stores, experiment tracking, and real-time performance monitoring to enable scalable, reliable machine learning operations in production environments.
- "PyPI (Python Package Index) is the official repository for Python packages, allowing developers to publish and install reusable code libraries to streamline development and promote modularity."
- A well-organized project FOLDER STRUCTURE with packages is essential to ensure modularity, scalability, and maintainability of code in a production-ready machine learning pipeline.


### template.py
- The script automates the creation of a well-structured Python project directory—especially useful for machine learning or backend applications. It ensures all required folders and files exist, and it does so safely, cleanly, and idempotently (can run multiple times without harm).

### "Ensure the project runs exactly the same today, tomorrow, and on another machine."
### Create Conda Environment (Basic Command)
- conda create --name us_visa_env python=3.10 -y
- conda activate us_visa_env

### setup.py
- It makes a Python project installable, reusable, and ready for distribution or deployment by defining its metadata and dependencies.
- requirements.txt (pip install -r requirements.txt)
- The -r flag is required to indicate you want pip to install from a requirements file, not a single package by that name. It helps automate dependency management and maintain consistency across environments.
- What Does -e . Mean? -- e stands for editable. -- . refers to the current directory (where setup.py is located).

### Workflow:
- Data Ingestion
- Data Validation
- Data Transformation
- Model Trainer
- Model Evaluation
- Model Pusher

### Steps to updation:
(constants ---> entity ---> components ---> pipeline ---> main.py)

### Data Ingestion
- Update Configuration Entity: The configuration module is well-structured, leveraging @dataclass to manage settings for each pipeline component, which is an excellent pattern for clean, type-safe, and extensible configuration management.
- Update artifact entity: The DataIngestionArtifact class holds paths to files generated during data ingestion.

    - Fields:
    - trained_file_path: Path to the training data file.
    - test_file_path: Path to the testing data file.