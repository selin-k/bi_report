## PythonPackageName

```solar_kpi_dashboard```

## DependenciesandTools

- ['pandas', 'For data loading and manipulation tasks such as data ingestion, curation, and transformation.']
- ['pyarrow', 'To support parquet file format operations during data curation and storage.']
- ['flask', 'To create the web application and API endpoints for microservices.']
- ['apache-airflow', 'To create automated workflows and orchestration of the ETL pipeline.']
- ['plotly', 'To create interactive visualizations for the dashboard.']
- ['azure-storage-blob', 'To interact with Azure Blob Storage for storing data in the data lake.']
- ['azure-identity', 'To authenticate with Azure services.']
- ['azure-synapse-spark', 'To submit and manage Spark jobs on Azure Synapse Analytics.']

## RequiredPythonPackages


pandas==1.3.4
pyarrow==5.0.0
flask==2.0.2
apache-airflow==2.2.3
plotly==5.3.1
azure-storage-blob==12.9.0
azure-identity==1.7.1
azure-synapse-spark==0.6.0


## TaskList

- ['main.py', 'Contains the orchestration logic for creating the dashboard with curated data and metrics. It initializes the Flask application and registers the microservices as blueprints. It also sets up the Apache Airflow DAG to schedule the ETL pipeline.']
- ['README.md', 'Contains a description of the project, its architecture, and instructions on how to set up, configure, and run the microservices.']
- ['config/config.yaml', 'Contains the configuration for the data ingestion framework. The configurations include parameters such as ProjectName, DataSource, SourcePath, SourceName, DataType, UserName, and Password.']
- ['config/config.py', 'Contains a singleton Config class that loads the config.yaml file for easy access throughout the framework. This class will be used by all microservices to access configuration settings.']
- ['data_ingest/data_ingestion.py', "Implements the DataIngestion class for orchestrating the data ingestion process. This class will be used by the DataIngestion microservice to ingest data from various sources and store it in the 'raw' data lake folder."]
- ['data_ingest/data_adaptor.py', 'Implements the DataAdaptor sub-component with several data adaptors for different data sources. It will include methods to connect to and fetch data from APIs, databases, local folders, and Azure Data Lake folders.']
- ['data_curate/data_curation.py', "Contains the logic for data curation. It will load raw data, remove duplicates, replace nulls, and map source data to target data. The curated data will be stored as a parquet table in the 'curated' data lake folder."]
- ['data_transformation/data_transformation.py', 'Implements the DataTransformation class for transforming curated data into a star schema format with fact and dimension tables. It will also calculate the KPIs defined in the requirements.']
- ['data_visualization/dashboard.py', 'Contains the logic for creating interactive visualizations using Plotly. It will load conformed data and generate line graphs, bar charts, and heat maps based on the KPIs.']
- ['orchestration/orchestration.py', 'Contains the main starter file logic to ensure Apache Airflow creates a DAG for the data pipeline, orchestrating the REST APIs from each microservice in sequence.']
- ['data_models/star_schema.py', 'Contains the logical data model definitions for the star schema, including fact and dimension tables used during data transformation.']

## FullAPISpec


```
openapi: 3.0.0
info:
  title: "Solar Panel KPI Dashboard API"
  version: "1.0.0"
paths:
  /ingest:
    post:
      summary: "Ingest data from configured data sources"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                ProjectName:
                  type: string
                DataSource:
                  type: string
                SourcePath:
                  type: string
                SourceName:
                  type: string
                DataType:
                  type: string
                UserName:
                  type: string
                Password:
                  type: string
      responses:
        '200':
          description: "Data ingestion successful"
  /curate:
    post:
      summary: "Curate ingested data"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                CuratedData:
                  type: string
      responses:
        '200':
          description: "Data curation successful"
  /transform:
    post:
      summary: "Transform curated data into star schema format"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                StarSchemaData:
                  type: string
      responses:
        '200':
          description: "Data transformation successful"
  /visualize:
    post:
      summary: "Generate visualizations from transformed data"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                VisualizationData:
                  type: string
      responses:
        '200':
          description: "Data visualization successful"
```


## AnythingUnclear

We need to clarify the specifics of the KPIs to be calculated during the DataTransformation process and the details of the interactive elements required for the DataVisualization microservice.

