"""
cell_culture_automation.py
Author: Victoria Langley
Description: This script automates the scheduling and management of cell culture experiments.
"""

import datetime

class CellCultureAutomation:
    def __init__(self):
        self.experiment_schedule = {}

    def schedule_experiment(self, cell_line, start_time, duration_hours):
        experiment_info = {"cell_line": cell_line, "start_time": start_time, "duration_hours": duration_hours}
        self.experiment_schedule[start_time] = experiment_info

    def view_schedule(self):
        print("Scheduled Cell Culture Experiments:")
        for start_time, experiment_info in self.experiment_schedule.items():
            print(f"{start_time}: {experiment_info['cell_line']} (Duration: {experiment_info['duration_hours']} hours)")

if __name__ == "__main__":
    automation = CellCultureAutomation()

    automation.schedule_experiment("HeLa", datetime.datetime(2023, 8, 15, 10, 0), 6)
    automation.schedule_experiment("CHO", datetime.datetime(2023, 8, 16, 14, 0), 8)
    automation.schedule_experiment("HEK293", datetime.datetime(2023, 8, 17, 9, 0), 5)

    automation.view_schedule()
