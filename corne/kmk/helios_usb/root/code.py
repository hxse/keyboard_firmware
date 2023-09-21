import sys

sys.path.append("helios_usb")  # 这样就可以直接引用keyboard文件夹里的文件

from helios_usb.run_keyboard import run_keyboard

run_keyboard()
