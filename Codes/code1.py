import board
from digitalio import DigitalInOut, Direction, Pull

#configuration des entrées sorties
Feu1Vert = DigitalInOut(board.GP16)
Feu1Vert.direction = Direction.OUTPUT
BP_Pieton1 = DigitalInOut(board.GP14)
BP_Pieton1.direction = Direction.INPUT
BP_Pieton1.pull = Pull.UP

while True :
    Feu1Vert.value = not BP_Pieton1.value
