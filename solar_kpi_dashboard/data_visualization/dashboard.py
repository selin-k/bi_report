# filename: solar_kpi_dashboard/data_visualization/dashboard.py
import os
import pandas as pd
import plotly.express as px
from ..config.config import Config

class Dashboard:
    def __init__(self):
        self.config = Config().settings

    def create_visualizations(self, kpis):
        # Create visualizations based on the KPIs
        # Placeholder for visualization logic
        # This should be implemented based on the specific visualization requirements

        # Example visualization using Plotly (to be replaced with actual logic)
        fig = px.bar(kpis, x='KPI Name', y='Value', title='KPI Visualization')
        fig.show()

    def load_transformed_data(self):
        # Load the transformed data from the 'conformed' data lake folder
        conformed_data_folder = os.path.join('data_lake', 'conformed', self.config['ProjectName'])
        fact_table_path = os.path.join(conformed_data_folder, 'fact_table.parquet')
        fact_table = pd.read_parquet(fact_table_path)
        return fact_table

# Example usage:
# dashboard_service = Dashboard()
# fact_table = dashboard_service.load_transformed_data()
# kpis = {'KPI Name': ['Total Energy Produced'], 'Value': [fact_table['energy_produced'].sum()]}
# dashboard_service.create_visualizations(kpis)