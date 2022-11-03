class Resistor:

    def __init__(self,ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
    def __repr__(self):
        return f'Resistor -> {self.__class__}(ohms={self.ohms}, voltage: {self.voltage})'

