from chicken_disease_classify.config.configuration import ConfigurationManager
from chicken_disease_classify.components.data_ingestion import DataIngestion
from chicken_disease_classify import logger

STAGE_NAME = "Data ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e
