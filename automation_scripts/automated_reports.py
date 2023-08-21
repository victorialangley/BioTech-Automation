"""
automated_reports.py
Author: Victoria Langley
Description: This script generates automated reports for biotech experiments.
"""

import os
import pandas as pd
from datetime import datetime

def generate_experiment_report(experiment_data_file, output_directory):
    # Load experiment data
    data = pd.read_csv(experiment_data_file)

    # Generate report
    report_content = f"Experiment Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report_content += "-" * 50 + "\n"
    report_content += f"Number of samples: {len(data)}\n"
    report_content += f"Mean value: {data['value'].mean()}\n"
    report_content += f"Standard deviation: {data['value'].std()}\n"

    # Save report
    report_filename = os.path.join(output_directory, "experiment_report.txt")
    with open(report_filename, "w") as report_file:
        report_file.write(report_content)
    
    print(f"Automated experiment report generated: {report_filename}")

if __name__ == "__main__":
    experiment_data_file = "experiment_data.csv"
    output_directory = "reports"
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    generate_experiment_report(experiment_data_file, output_directory)
