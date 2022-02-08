from abc import ABC
class Battery(ABC):
    def __init__(self,current_date,last_service_date):
        self.current_date=current_date
        self.last_service_date=last_service_date
        
    def battery_should_be_serviced(self):
        pass