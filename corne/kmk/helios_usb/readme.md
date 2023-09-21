# corne kmk
* find circuitpython for your board
  * https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython
  * https://circuitpython.org/downloads
  * https://circuitpython.org/board/0xcb_helios/
* copy code lines to code.py and put it on CIRCUITPY drive root path.
  ```
  import sys
  sys.path.append("helios_usb") # 这样就可以直接引用keyboard文件夹里的文件

  from helios_usb.run_keyboard import run_keyboard
  run_keyboard()
  ```
* copy code lines to boot.py and put it on CIRCUITPY drive root path.
  ```
  import usb_cdc

  usb_cdc.enable(data=True)
  ```
* copy Libs to root path
  * copy dir: https://github.com/KMKfw/kmk_firmware/tree/master/kmk
  * copy file: https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py
  * copy file: https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306/blob/main/adafruit_displayio_ssd1306.py
  * copy dir: https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/tree/main/adafruit_display_text
* 还是有问题, 根据layer切换rgb时, 左手只能切换左边, 右手可以切换两边,很奇怪,算了用qmk吧
