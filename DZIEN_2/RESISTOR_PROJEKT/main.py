from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistor
from bounded import BoundedResistance

print("_____________klasa OldResistor____________________")

r0 = OldResistor(10.3E2)
print(r0)
print(r0._ohms)
r0._ohms = 2.66E2
print(r0._ohms)
r0.set_ohms(4.5E3)
print(r0._ohms)
print(r0.get_ohms())

print("_______________klasa Resistor__________________")

r1 = Resistor(1e3)
r1.ohms = 10E3
print(f'układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A')

print("_______________klasa VoltageResistor__________________")

r2 = VoltageResistor(2.7E3)
print(f'natężenie początkowe prądu: {r2.current} A')
print(f'napięcie początkowe prądu: {r2.voltage} V')
print(f'napięcie początkowe prądu: {r2._voltage} V')
r2.voltage = 25
print(f'natężenie prądu: {r2.current} A')
print(f'napięcie: {r2.voltage} V')
print(r2._voltage)
print({r2})


print("_______________klasa BoundedResistance__________________")
try:
      r3 = BoundedResistance(2E2)
      r3.ohms = 12
      print(f'oporność: {r3.ohms}')
      print(r3)
except ValueError as fg:
      print(fg)






