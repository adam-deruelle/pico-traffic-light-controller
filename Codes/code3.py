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
#Feu2Vert
Feu2Vert = DigitalInOut(board.GP18)
Feu2Vert.direction = Direction.OUTPUT
#Feu2Orange
Feu2Orange = DigitalInOut(board.GP18)
Feu2Orange.direction = Direction.OUTPUT
#Feu2Rouge
Feu2Rouge = DigitalInOut(board.GP18)
Feu2Rouge.direction = Direction.OUTPUT

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
#Menu
BP_Menu = DigitalInOut(board.GP20)
BP_Menu.direction = Direction.INPUT
BP_Menu.pull = Pull.UP
#Plus
BP_Plus = DigitalInOut(board.GP20)
BP_Plus.direction = Direction.INPUT
BP_Plus.pull = Pull.UP
#Moins
BP_Moins = DigitalInOut(board.GP20)
BP_Moins.direction = Direction.INPUT
BP_Moins.pull = Pull.UP

## instanciation
Timer1Vert = TON()
Timer1Orange = TON()
Timer1Rouge = TON()

Timer2Vert = TON()
Timer2Orange = TON()
Timer2Rouge = TON()

## initialisation de l'automate
X0 = 1
X10 = 0
X20 = 0
X30 = 0

while True:
    #mise à jour du timer
    Timer1Vert.maj(5)
    Timer1Orange.maj(1)
    
    Timer2Vert.maj(5)
    Timer2Orange.maj(1)

    #les conditions d'évolution
    CE0_10 = Timer1Vert.Q and X0
    CE10_20 = Timer1Orange.Q and X10
    CE20_30 = Timer2Vert.Q and X20
    CE30_0 = Timer2Orange.Q and X30

    #les étapes
    if CE0_10 :
        X10=1
        X0=0
    if CE10_20 :
        X20=1
        X10=0
    if CE20_30 :
        X30=1
        X20=0
    if CE30_0 :
        X0=1
        X30=0

    #les actions
    Feu1Vert.value = X0
    Feu1Orange.value = X10
    Feu1Rouge.value = X20 or X30

    Timer1Vert.IN = X0
    Timer1Orange.IN = X10
    Timer1Rouge.IN = X20 or X30

    Feu2Vert.value = X20
    Feu2Orange.value = X30
    Feu2Rouge.value = X0 or X10

    Timer2Vert.IN = X20
    Timer2Orange.IN = X30
    Timer2Rouge.IN = X0 or X10
