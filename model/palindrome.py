from datetime import datetime
from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(SternmanEngine,SpindlerBattery):
    def needs_service(self):
        #service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
