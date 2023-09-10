# piantor_kmk_firmware
Copy code lines in code.py and put it on CIRCUITPY drive. Or cut code.py to CIRCUITPY root drive.
```
import sys
sys.path.append("piantor_kmk_firmware") # 这样就可以直接引用keyboard文件夹里的文件

from piantor_kmk_firmware.run_keyboard import run_keyboard
run_keyboard()
```

# PC code
  * https://github.com/hxse/py-active-windows-keyboard/blob/main/send_kmk.py

# piantor:
https://docs.beekeeb.com/piantor-keyboard
https://github.com/beekeeb/piantor
https://www.pcbway.com/project/shareproject/Piantor_Keyboard_Left_side_24a2937f.html
https://www.pcbway.com/project/shareproject/Piantor_Keyboard_Right_side_7c5b31eb.html

# 其他键盘:
https://github.com/foostan/crkbd

# 刷circuitpython:
https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython
https://circuitpython.org/board/raspberry_pi_pico/

# 复制kmk库:
http://kmkfw.io/docs/Getting_Started
https://github.com/KMKfw/kmk_firmware

# 写kmk代码:
分体键盘需要每个主控, 都要走流程, 刷circuitpython -> 复制kmk库 ->写kmk代码
但是更改配列只需要改左手的kmk代码就行了, 右手不用改, 不用动, 但是得有
kmk代码文件在评论区

# 参考:
https://github.com/cairnm/kmk_firmware/tree/piantor/boards/beekeeb/piantor
https://github.com/KMKfw/kmk_firmware/issues/869
https://pyserial.readthedocs.io/en/latest/shortintro.html
