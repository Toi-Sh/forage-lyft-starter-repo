from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_list):
        self.tire_list=tire_list

    def needs_service(self):
        for tire in self.tire_list:
            if tire>=0.9:
                return True
           
        return False

        