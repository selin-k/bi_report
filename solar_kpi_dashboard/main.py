# filename: solar_kpi_dashboard/main.py
from flask import Flask
# Importing the blueprint classes from microservices (to be implemented)
# from data_ingest.data_ingestion import data_ingestion_blueprint
# from data_curate.data_curation import data_curation_blueprint
# from data_transformation.data_transformation import data_transformation_blueprint
# from data_visualization.dashboard import dashboard_blueprint

# Initialize the Flask application
app = Flask(__name__)

# Register the blueprints for each microservice (placeholders for now)
# app.register_blueprint(data_ingestion_blueprint)
# app.register_blueprint(data_curation_blueprint)
# app.register_blueprint(data_transformation_blueprint)
# app.register_blueprint(dashboard_blueprint)

# Setup the Apache Airflow DAG (placeholder for now)
# This will be implemented once the microservices are ready

# Define the main entry point for the Flask application
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)