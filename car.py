from abc import ABC, abstractmethod
from engine import engine
from engine.Engine import Engine



class Car(ABC):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date=current_date
        self.last_service_date=last_service_date
        self.current_mileage=current_mileage
        self.last_service_mileage = last_service_mileage
        engine=""
        battery=""


    @abstractmethod
    def needs_service(self):
        pass
    def create_calliope(self):
        self.engine="Capulet Engine"
        self.battery="Spindler Battery"
        
    def create_glissade(self):
        self.engine="Willoughby Engine"
        self.battery="Spindler Battery"