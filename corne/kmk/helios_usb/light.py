from kmk.extensions.rgb import RGB

from kmk.extensions.peg_oled_Display import (
    Oled,
    OledDisplayMode,
    OledReactionType,
    OledData,
)

from kb import KMKKeyboard, isRight

keyboard = KMKKeyboard()

rgb = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=27,
    hue_default=int(255 * 0.99),
    sat_default=int(255 * 0.86),
    val_default=int(255 * 0.038),
)

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
