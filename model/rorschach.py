from datetime import datetime
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery

class Rorschach(WilloughbyEngine,NubbinBattery):
    def needs_service(self):
        #service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
