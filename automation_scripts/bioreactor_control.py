"""
bioreactor_control.py
Author: Victoria Langley
Description: This script simulates the control of a bioreactor's temperature and agitation speed.
"""

import random
import time

class Bioreactor:
    def __init__(self):
        self.temperature = 25.0
        self.agitation_speed = 200

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Bioreactor temperature set to {temperature}°C")

    def set_agitation_speed(self, speed):
        self.agitation_speed = speed
        print(f"Agitation speed set to {speed} RPM")

    def run(self):
        print("Bioreactor started")
        while True:
            self._adjust_parameters()
            time.sleep(5)

    def _adjust_parameters(self):
        self.temperature = self._random_variation(self.temperature, 0.5)
        self.agitation_speed = self._random_variation(self.agitation_speed, 10)

        print(f"Temperature: {self.temperature}°C, Agitation Speed: {self.agitation_speed} RPM")

    def _random_variation(self, value, max_change):
        variation = random.uniform(-max_change, max_change)
        return value + variation

if __name__ == "__main__":
    bioreactor = Bioreactor()
    bioreactor.run()
