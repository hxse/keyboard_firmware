from kmk.extensions.rgb import RGB

from kmk.extensions.peg_oled_Display import (
    Oled,
    OledDisplayMode,
    OledReactionType,
    OledData,
)

from kb import KMKKeyboard

rgb = RGB(
    pixel_pin=KMKKeyboard.rgb_pixel_pin,
    num_pixels=27,
    hue_default=int(255 * 0.99),
    sat_default=int(255 * 0.86),
    val_default=int(255 * 0.038),
)

from kmk.modules.layers import Layers


rgb_list = [
    [130, 185, 30],
    [254, 240, 37],
    [105, 160, 16],
    [105, 160, 16],
    [11, 210, 23],
    [11, 210, 23],
    [70, 180, 28],
]


def set_hsv(l):
    rgb.set_hsv_fill(*[int(i) for i in l])


class RgbSwitchLayers(Layers):
    last_top_layer = 0
    hues = (4, 20, 69)

    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            if keyboard.active_layers[0] < len(rgb_list) - 1:
                set_hsv(rgb_list[keyboard.active_layers[0]])
            else:
                set_hsv(rgb_list[-1])


oled_text = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ["layer"]},
        corner_two={
            0: OledReactionType.LAYER,
            1: [
                "0_game",
                "1_qwert",
                "2_cursor",
                "3_symbol",
                "4_fn",
                "5_pad_str",
                "6_rgb",
                "7",
                "8",
                "9",
                "10",
            ],
        },
        corner_three={
            0: OledReactionType.LAYER,
            1: [
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ],
        },
        corner_four={
            0: OledReactionType.LAYER,
            1: [
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ],
        },
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)

oled_display_data = OledData(
    image={
        0: OledReactionType.LAYER,
        1: [
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
            "helios_usb/logo.bmp",
        ],
    }
)
oled_image = Oled(oled_display_data, toDisplay=OledDisplayMode.IMG, flip=False)
