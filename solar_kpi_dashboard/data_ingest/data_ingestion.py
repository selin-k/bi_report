# filename: solar_kpi_dashboard/data_ingest/data_ingestion.py
from datetime import datetime
import os
import pandas as pd
from ..config.config import Config
from .data_adaptor import DataAdaptor  # This will be implemented later

class DataIngestion:
    def __init__(self):
        self.config = Config().settings
        self.data_adaptor = DataAdaptor(self.config)

    def ingest_data(self):
        # Create a folder for the current date under the "raw" folder
        date_folder = datetime.now().strftime('%Y-%m-%d')
        raw_data_folder = os.path.join('data_lake', 'raw', date_folder)
        os.makedirs(raw_data_folder, exist_ok=True)

        # Use the DataAdaptor to fetch data from the configured data source
        data = self.data_adaptor.fetch_data()

        # If the data is not in CSV format, convert it to CSV
        if self.config['DataType'].lower() != 'csv':
            data = self.convert_to_csv(data)

        # Save the data to the "raw" data folder for the current date
        file_path = os.path.join(raw_data_folder, self.config['SourceName'] + '.csv')
        data.to_csv(file_path, index=False)

    def convert_to_csv(self, data):
        # Convert data to CSV format
        if isinstance(data, pd.DataFrame):
            return data
        else:
            # Implement conversion for other data types if necessary
            raise NotImplementedError("Data conversion for the specified type is not implemented.")

# Example usage:
# data_ingestion_service = DataIngestion()
# data_ingestion_service.ingest_data()