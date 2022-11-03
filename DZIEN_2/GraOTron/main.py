from tywin import Tywin
from tyrion import Tyrion
from cersei import Cersei

tyw = Tywin("Lannister","Lord","m",3,8,9)
tyr = Tyrion("Lannister","Lord","m",5,10,8)
cer = Cersei("Lannister","Królowa","k",3,10,10)

print(tyw)
tyw.walka()
tyw.negocjacja()
tyw.uczta()

print(tyr)
tyr.walka()
tyr.negocjacja()
tyr.uczta()

print(cer)
cer.walka()
cer.negocjacja()
cer.uczta()
