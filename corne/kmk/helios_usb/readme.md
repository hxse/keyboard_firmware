# corne kmk
* copy kmk dir to root: https://github.com/KMKfw/kmk_firmware/tree/master/kmk
* copy neopixel to root: https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py
* Copy code lines in code.py and put it on CIRCUITPY drive. Or cut code.py to CIRCUITPY root drive.
```
import sys
sys.path.append("helios_usb") # 这样就可以直接引用keyboard文件夹里的文件

from helios_usb.run_keyboard import run_keyboard
run_keyboard()
```
* copy Libs to root path
  * https://github.com/KMKfw/kmk_firmware/tree/master/kmk
  * https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py
  * https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306/blob/main/adafruit_displayio_ssd1306.py
  * https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/tree/main/adafruit_display_text
* 先用qmk吧, 有个bug未解决
