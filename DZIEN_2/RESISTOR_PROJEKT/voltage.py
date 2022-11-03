from resistor import Resistor

class VoltageResistor(Resistor):

    def __init__(self,ohms):
        super().__init__(ohms)
        self._voltage = 5

    def __repr__(self):
        return f'VoltageResistor(ohms={self.ohms}, voltage: {self.voltage})'

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self,voltage):
        self._voltage = voltage
        self.current = self._voltage/self.ohms
