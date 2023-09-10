import sys, os

import board
import digitalio


from kb import KMKKeyboard, isRight

from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.oneshot import OneShot

print("start")

keyboard = KMKKeyboard()
keyboard.tap_time = 100
keyboard.debug_enabled = False


layers = Layers()

split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT

data_pin = board.GP1 if split_side == SplitSide.LEFT else board.GP0
data_pin2 = board.GP0 if split_side == SplitSide.LEFT else board.GP1

split = Split(
    split_side=split_side,
    split_type=SplitType.UART,
    split_flip=False,
    data_pin=data_pin,
    data_pin2=data_pin2,
)

mousekyes = MouseKeys()

oneshot = OneShot()
# optional: set a custom tap timeout in ms (default: 1000ms)
# oneshot.tap_time = 1500

keyboard.modules = [layers, split, mousekyes, oneshot]
keyboard.extensions.append(MediaKeys())

from key_map import keymap

keyboard.keymap = keymap


def run_keyboard():
    from serialace2 import SerialACE

    keyboard.modules.append(SerialACE())

    print("end")
    keyboard.go()


if __name__ == "__main__":
    run_keyboard()
