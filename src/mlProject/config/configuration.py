from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml, create_directories
from src.mlProject.entity.config_entity import DataIngestionConfig
from src.mlProject.entity.config_entity import DataValidationConfig
from src.mlProject.entity.config_entity import DataTransformationConfig
from src.mlProject.entity.config_entity import ModelTrainerConfig
from src.mlProject.entity.config_entity import ModelEvaluationConfig


class ConfigurationManager:
    """
    Manages configuration for the ML pipeline components.
    
    This class centralizes access to all configuration parameters by reading from
    YAML configuration files and providing component-specific configuration objects.
    
    Attributes:
        config: Main configuration parameters from config.yaml
        params: Model hyperparameters and training parameters from params.yaml
        schema: Data schema specifications from schema.yaml
    
    Methods:
        get_data_ingestion_config: Returns configuration for the data ingestion component
    """
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):
        """
        Initialize the ConfigurationManager with paths to configuration files.
        
        Args:
            config_filepath: Path to the main configuration file (default: CONFIG_FILE_PATH)
            params_filepath: Path to the parameters file (default: PARAMS_FILE_PATH)
            schema_filepath: Path to the schema file (default: SCHEMA_FILE_PATH)
        
        Note:
            Creates the root artifacts directory specified in the main configuration.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Prepare and return the configuration for data ingestion.
        
        Returns:
            DataIngestionConfig: Configuration object with all parameters
                                 required for the data ingestion component.
                                 
        Note:
            Creates the root directory for data ingestion if it doesn't exist.
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Prepare and return the configuration for data validation.
        
        This method extracts the data validation configuration from the config file
        and the column schema from the schema file, then combines them into a
        DataValidationConfig object.
        
        Returns:
            DataValidationConfig: Configuration object with all parameters
                                 required for the data validation component.
                                 
        Note:
            Creates the root directory for data validation if it doesn't exist.
            The schema.COLUMNS is passed as all_schema to validate data types.
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Prepare and return the configuration for data transformation.
        
        This method extracts the data transformation configuration from the config file
        and creates a DataTransformationConfig object.
        
        Returns:
            DataTransformationConfig: Configuration object with all parameters
                                     required for the data transformation component.
                                     
        Note:
            Creates the root directory for data transformation if it doesn't exist.
        """
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Prepare and return the configuration for model training.
        
        This method combines information from three sources:
        1. config.yaml - For file paths related to training
        2. params.yaml - For model hyperparameters 
        3. schema.yaml - For the target column name
        
        Returns:
            ModelTrainerConfig: Configuration object with all parameters
                                required for the model training component.
                                
        Note:
            Creates the root directory for model training if it doesn't exist.
            This is the only configuration method that pulls from all three
            configuration sources.
        """
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
        )

        return model_trainer_config
    
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Prepare and return the configuration for model evaluation.
        
        This method combines information from three sources:
        1. config.yaml - For file paths related to evaluation
        2. params.yaml - For model hyperparameters to document with metrics
        3. schema.yaml - For the target column name
        
        Returns:
            ModelEvaluationConfig: Configuration object with all parameters
                                  required for the model evaluation component.
                                  
        Note:
            Creates the root directory for model evaluation if it doesn't exist.
            Includes the complete hyperparameter dictionary in the configuration
            to enable tracking parameters alongside performance metrics.
        """
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column=schema.name
        )

        return model_evaluation_config