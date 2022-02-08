from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tires_list):
        self.engine = engine
        self.battery = battery
        self.tires_list=tires_list

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires_list.needs_service()