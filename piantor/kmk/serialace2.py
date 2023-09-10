from usb_cdc import data

from kmk.modules import Module
from kmk.utils import Debug
from kmk.keys import KC

debug = Debug(__name__)


def callback(keyboard, data: bytearray):
    # 虽然发送时要加\n,但callback接受时已经被自动清理掉\n了,callback返回时也不用添加\n,因为会被自动加上\n
    # 格式是b'args1 args2 args3', 一般args1是mode, 后面的args是参数
    print("receive", data)
    text: str = "".join([chr(i) for i in data])
    args = text.split(" ")

    if args[0] == "switch_layer":
        num = int(args[1])
        keyboard.tap_key(KC.TO(num))
        return f"success: {text}"

    return


class SerialACE(Module):
    buffer = bytearray()

    def during_bootup(self, keyboard):
        keyboard.tap_key(KC.DF(1))
        try:
            data.timeout = 0
        except AttributeError:
            pass

    def before_matrix_scan(self, keyboard):
        pass

    def after_matrix_scan(self, keyboard):
        # keyboard.tap_key(KC.DF(1))
        pass

    def process_key(self, keyboard, key, is_pressed, int_coord):
        return key

    def before_hid_send(self, keyboard):
        # Serial.data isn't initialized.
        if not data:
            return

        # Nothing to parse.
        if data.in_waiting == 0:
            return

        self.buffer.extend(data.read())
        idx = self.buffer.find(b"\n")

        # No full command yet.
        if idx == -1:
            return

        # Split off command and evaluate.
        line = self.buffer[:idx]
        self.buffer = self.buffer[idx + 1 :]

        try:
            if debug.enabled:
                debug(f"eval({line})")

            # ret = eval(line, {'keyboard': keyboard,'KC':KC})
            # eval太危险了,在callback里自己定义吧

            res = callback(keyboard, line)

            data.write(bytearray(str(res) + "\n"))
        except Exception as err:
            if debug.enabled:
                debug(f"error: {err}")
            data.write(bytearray("error: " + str(err) + "\n"))

    def after_hid_send(self, keyboard):
        pass

    def on_powersave_enable(self, keyboard):
        pass

    def on_powersave_disable(self, keyboard):
        pass
