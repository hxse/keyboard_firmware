import sys, os

import board
import digitalio


from kb import KMKKeyboard, isRight

from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.oneshot import OneShot

from light import rgb, oled_text, oled_image, RgbSwitchLayers

keyboard = KMKKeyboard()
keyboard.debug_enabled = False


layers = Layers()
layers = RgbSwitchLayers()

split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT
oled_ext = oled_text if not isRight else oled_image


split = Split(
    split_side=split_side,
    use_pio=True,  # https://github.com/KMKfw/kmk_firmware/issues/878
)


mousekyes = MouseKeys()

oneshot = OneShot()
mediaKeys = MediaKeys()

keyboard.modules = keyboard.modules + [layers, split, mousekyes, oneshot]
keyboard.extensions = keyboard.extensions + [mediaKeys, rgb, oled_ext]

from key_map import keymap

keyboard.keymap = keymap


def run_keyboard():
    from serialace2 import SerialACE

    serialACE = SerialACE()
    keyboard.modules.append(serialACE)

    keyboard.go()


if __name__ == "__main__":
    run_keyboard()
