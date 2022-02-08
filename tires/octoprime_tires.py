from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_list):
        self.tire_list=tire_list

    def needs_service(self):
        if sum(self.tire_list)>=3:
            return True
        else:
            return False

        