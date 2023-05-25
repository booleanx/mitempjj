from jchart.config import Axes, DataSet, rgba
from jchart import Chart
import collections
import statistics
from datetime import datetime, timedelta
import sqlite3


SQLITE_DB_PATH = "./../database/mitempjj.db"

class LineChart(Chart):
    '''All charts in one'''

    def __init__(self, start_date, stop_date):
        self.start_date = start_date
        self.stop_date = stop_date
        super().__init__()

    chart_type = 'line'

    def get_datasets(self, **kwargs):
        colors = [
            rgba(255, 99, 132, 0.2),
            rgba(54, 162, 235, 0.2),
            rgba(255, 206, 86, 0.2),
            rgba(75, 192, 192, 0.2),
            rgba(153, 102, 255, 0.2),
            rgba(255, 159, 64, 0.2)
        ]
        sensor_names = get_sensor_names()  # Get all sensor names
        datasets = []

        for i, sensor_name in enumerate(sensor_names):
            dataset = {
                'label': [sensor_name],  # Use sensor name as label
                'backgroundColor': colors[i % len(colors)],
                'borderColor': colors[i % len(colors)],
                'data': readall(StartDate=self.start_date, EndDate=self.stop_date, sensor_name=sensor_name).get(
                    'temperaturetab')
            }
            datasets.append(dataset)

        return datasets

    def get_labels(self, **kwargs):
        # Get labels from any dataset, assuming all datasets have the same labels
        sensor_names = get_sensor_names()
        first_sensor_name = sensor_names[0] if sensor_names else ''
        return readall(StartDate=self.start_date, EndDate=self.stop_date, sensor_name=first_sensor_name).get('datetab')
