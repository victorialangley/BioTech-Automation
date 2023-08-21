"""
lab_experiment_scheduler.py
Author: Victoria Langley
Description: This script automates the scheduling of various lab experiments.
"""

import heapq
import datetime

class LabExperimentScheduler:
    def __init__(self):
        self.experiment_heap = []

    def schedule_experiment(self, experiment_name, start_time):
        heapq.heappush(self.experiment_heap, (start_time, experiment_name))

    def view_schedule(self):
        print("Scheduled Lab Experiments:")
        for start_time, experiment_name in self.experiment_heap:
            print(f"{start_time}: {experiment_name}")

if __name__ == "__main__":
    scheduler = LabExperimentScheduler()

    scheduler.schedule_experiment("PCR Analysis", datetime.datetime(2023, 8, 20, 9, 0))
    scheduler.schedule_experiment("Gel Electrophoresis", datetime.datetime(2023, 8, 21, 14, 0))
    scheduler.schedule_experiment("Enzyme Assay", datetime.datetime(2023, 8, 22, 11, 0))

    scheduler.view_schedule()
