import board
import time
from timer import TON
from digitalio import DigitalInOut, Direction, Pull

## configuration des entrées sorties
#FeuVert
Feu1Vert = DigitalInOut(board.GP16)
Feu1Vert.direction = Direction.OUTPUT
#FeuOrange
Feu1Orange = DigitalInOut(board.GP17)
Feu1Orange.direction = Direction.OUTPUT
#FeuRouge
Feu1Rouge = DigitalInOut(board.GP18)
Feu1Rouge.direction = Direction.OUTPUT

#Pieton1
BP_Pieton1 = DigitalInOut(board.GP14)
BP_Pieton1.direction = Direction.INPUT
BP_Pieton1.pull = Pull.UP
#Pieton2
BP_Pieton2 = DigitalInOut(board.GP19)
BP_Pieton2.direction = Direction.INPUT
BP_Pieton2.pull = Pull.UP
#Mag
BoucleMag = DigitalInOut(board.GP20)
BoucleMag.direction = Direction.INPUT
BoucleMag.pull = Pull.UP

## instanciation
Timer1Vert = TON()
Timer1Orange = TON()
Timer1Rouge = TON()

## initialisation de l'automate
X0 = 1
X10 = 0
X20 = 0

while True:
    #mise à jour du timer
    Timer1Vert.maj(5)
    Timer1Orange.maj(1)
    Timer1Rouge.maj(8)

    #les conditions d'évolution
    CE0_10 = Timer1Vert.Q and X0
    CE10_20 = Timer1Orange.Q and X10
    CE20_0 = Timer1Rouge.Q and X20

    #les étapes
    if CE0_10 :
        X10=1
        X0=0
    if CE10_20 :
        X20=1
        X10=0
    if CE20_0 :
        X0=1
        X20=0

    #les actions
    Feu1Vert.value = X0
    Feu1Orange.value = X10
    Feu1Rouge.value = X20
    Timer1Vert.IN = X0
    Timer1Orange.IN = X10
    Timer1Rouge.IN = X20
