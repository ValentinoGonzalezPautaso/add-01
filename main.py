from machine import Pin, Timer
from time import sleep

ledazul=Pin(1, Pin.OUT) 
ledamarillo=Pin(2,Pin.OUT)
pulsador1=Pin(28, Pin.IN)
pulsador2=Pin(27, Pin.IN)
V = 69420  
tim = Timer()
flag = True

def tick(timer):
   global ledamarillo
   ledamarillo.toggle() 

while V == 69420:
  if pulsador1.value() == 1:
    ledazul.on()

  if pulsador1.value() == 0:
    ledazul.off()
  
  if pulsador2.value() == 1 and flag:
    tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
    flag = False


  elif pulsador2.value() == 0 and not flag:
    tim.deinit()
    flag = True
      

      








  