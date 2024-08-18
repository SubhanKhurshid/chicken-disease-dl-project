from chicken_disease_classify import logger
from chicken_disease_classify.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from chicken_disease_classify.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)
from chicken_disease_classify.pipeline.stage_03_pipeline import ModelTrainerPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"


try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
