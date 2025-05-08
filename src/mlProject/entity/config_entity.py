from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for data ingestion with immutable attributes.
    
    This dataclass defines the required parameters for the data ingestion process
    in the wine quality prediction pipeline. The 'frozen=True' parameter ensures
    all attributes are read-only after initialization.
    
    Attributes:
        root_dir (Path): Directory where all data ingestion outputs will be stored
        source_URL (str): URL pointing to the source data to be downloaded
        local_data_file (Path): Path where the downloaded data file will be saved
        unzip_dir (Path): Directory where downloaded data will be extracted
    
    Note:
        Using Path objects instead of strings ensures cross-platform compatibility
        and provides helpful path manipulation methods.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration class for data validation with immutable attributes.
    
    This dataclass defines the required parameters for the data validation process
    in the wine quality prediction pipeline. The 'frozen=True' parameter ensures
    all attributes are read-only after initialization.
    
    Attributes:
        root_dir (Path): Directory where all data validation outputs will be stored
        STATUS_FILE (str): Path to the file that will contain validation status (True/False)
        unzip_data_dir (Path): Path to the CSV file to be validated (from data ingestion)
        all_schema (dict): Dictionary containing the expected schema information 
                          from schema.yaml, including column data types and target column
    
    Note:
        The validation process compares the actual dataset against the schema
        defined in all_schema to ensure data consistency and quality.
    """
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    

@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Configuration class for data transformation with immutable attributes.
    
    This dataclass defines the required parameters for the data transformation process
    in the wine quality prediction pipeline. The 'frozen=True' parameter ensures
    all attributes are read-only after initialization.
    
    Attributes:
        root_dir (Path): Directory where all data transformation outputs will be stored,
                        including preprocessed datasets and serialized transformers
        data_path (Path): Path to the validated CSV file that will be transformed,
                         output from the data ingestion step
    
    Note:
        Data transformation typically includes preprocessing steps like scaling,
        normalization, handling missing values, and train-test splitting, which
        prepare the data for model training.
    """
    root_dir: Path
    data_path: Path
    

@dataclass(frozen=True)
class ModelTrainerConfig:
    """
    Configuration class for model training with immutable attributes.
    
    This dataclass defines the required parameters for the model training process
    in the wine quality prediction pipeline. The 'frozen=True' parameter ensures
    all attributes are read-only after initialization.
    
    Attributes:
        root_dir (Path): Directory where all model training outputs will be stored,
                        including the trained model file and performance metrics
        train_data_path (Path): Path to the CSV file containing training data,
                               output from the data transformation step
        test_data_path (Path): Path to the CSV file containing testing data,
                              output from the data transformation step
        model_name (str): Filename for saving the trained model (typically model.joblib)
        alpha (float): Regularization strength parameter for the ElasticNet model,
                      controls the overall penalty applied to coefficients
        l1_ratio (float): The mix of L1 and L2 regularization in the ElasticNet model,
                         where 0 is Ridge (L2 only) and 1 is Lasso (L1 only)
        target_column (str): Name of the column to predict (the target variable),
                            typically "quality" for the wine quality prediction
    
    Note:
        This configuration combines paths from the config.yaml file and 
        hyperparameters from the params.yaml file into a single object
        for the model training component.
    """
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str
    
    
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    Configuration class for model evaluation with immutable attributes.
    
    This dataclass defines the required parameters for the model evaluation process
    in the wine quality prediction pipeline. The 'frozen=True' parameter ensures
    all attributes are read-only after initialization.
    
    Attributes:
        root_dir (Path): Directory where all model evaluation outputs will be stored,
                        including metrics and evaluation reports
        test_data_path (Path): Path to the CSV file containing testing data,
                              output from the data transformation step
        model_path (Path): Path to the trained model file (.joblib),
                          output from the model trainer step
        all_params (dict): Dictionary containing all hyperparameters used for training,
                          useful for documenting model configuration alongside metrics
        metric_file_name (Path): Path where evaluation metrics will be saved as JSON,
                                enables tracking performance across model iterations
        target_column (str): Name of the column being predicted (the target variable),
                            typically "quality" for the wine quality prediction
    
    Note:
        This configuration combines paths from the config.yaml file, 
        hyperparameters from the params.yaml file, and target information 
        from the schema.yaml file into a single object for the model 
        evaluation component.
    """
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str