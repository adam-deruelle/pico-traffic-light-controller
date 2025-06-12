import board
import time
from timer import TON
from digitalio import DigitalInOut, Direction, Pull
from maintenance import config_feux

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
Feu2Vert = DigitalInOut(board.GP27)
Feu2Vert.direction = Direction.OUTPUT
#Feu2Orange
Feu2Orange = DigitalInOut(board.GP26)
Feu2Orange.direction = Direction.OUTPUT
#Feu2Rouge
Feu2Rouge = DigitalInOut(board.GP22)
Feu2Rouge.direction = Direction.OUTPUT
#LED Jour
LedJour = DigitalInOut(board.LED)
LedJour.direction = Direction.OUTPUT

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
BP_Menu = DigitalInOut(board.GP12)
BP_Menu.direction = Direction.INPUT
BP_Menu.pull = Pull.UP
#Plus
BP_Plus = DigitalInOut(board.GP13)
BP_Plus.direction = Direction.INPUT
BP_Plus.pull = Pull.UP
#Moins
BP_Moins = DigitalInOut(board.GP11)
BP_Moins.direction = Direction.INPUT
BP_Moins.pull = Pull.UP

## instanciation
Timer1Vert = TON()
Timer1Orange = TON()
Timer1Rouge = TON()

Timer2Vert = TON()
Timer2Orange = TON()
Timer2Rouge = TON()

TimerJour = TON()
TimerNuit = TON()

## initialisation de l'automate
X0 = 1
X10 = 0
X100 = 1
X20 = 0
X200 = 0
X30 = 0
X40 = 0
X50 = 0
while True:
    config_feux(BP_Menu, BP_Plus, BP_Moins)
    #mise à jour du timer
    Timer1Vert.maj(5)
    Timer1Orange.maj(1)
    Timer1Rouge.maj(1)

    Timer2Vert.maj(5)
    Timer2Orange.maj(1)
    Timer2Rouge.maj(1)

    TimerJour.maj(20)
    TimerNuit.maj(20)

    #les conditions d'évolution
    CE0_10 = Timer1Vert.Q and X0 and (X100 or not BP_Pieton1.value or not BP_Pieton2.value or not BoucleMag.value)
    CE10_20 = Timer1Orange.Q and X10
    CE20_30 = Timer1Rouge.Q and X20
    CE30_40 = Timer2Vert.Q and X30
    CE40_50 = Timer2Orange.Q and X40
    CE50_0 = Timer2Rouge.Q and X50

    CE100_200 = TimerJour.Q and X100
    CE200_100 = TimerNuit.Q and X200

    #les étapes
    if CE0_10 :
        X10=1
        X0=0
    elif CE10_20 :
        X20=1
        X10=0
    elif CE20_30 :
        X30=1
        X20=0
    elif CE30_40 :
        X40=1
        X30=0
    elif CE40_50:
        X50=1
        X40=0
    elif CE50_0:
        X0=1
        X50=0

    if CE100_200 :
        X200=1
        X100=0
    elif CE200_100 :
        X100=1
        X200=0

    #les actions
    Feu1Vert.value = X0
    Feu1Orange.value = X10
    Feu1Rouge.value = X20 or X30 or X40 or X50

    Timer1Vert.IN = X0
    Timer1Orange.IN = X10
    Timer1Rouge.IN = X20 or X30

    Feu2Vert.value = X30
    Feu2Orange.value = X40
    Feu2Rouge.value = X0 or X10 or X20 or X50

    Timer2Vert.IN = X30
    Timer2Orange.IN = X40
    Timer2Rouge.IN = X0 or X10 or X50

    LedJour.value = X100

    TimerJour.IN = X100
    TimerNuit.IN = X200
