
from oldresistor import OldResistor

print("_________________________________")

r0 = OldResistor(10.3E2)
print(r0)
print(r0._ohms)
r0._ohms = 2.66E2
print(r0._ohms)
r0.set_ohms(4.5E3)
print(r0._ohms)
print(r0.get_ohms())

print("_________________________________")
