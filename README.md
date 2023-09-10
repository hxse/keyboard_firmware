# keyboard_firmware
## qmk firmware
  * 建议用vial-qmk https://github.com/vial-kb/vial-qmk/issues/538
  * corne和kmk好像也有冲突,可以用qmk https://github.com/KMKfw/kmk_firmware/issues/878
  * 下载qmk库: `git clone https://github.com/vial-kb/vial-qmk`
  * 设置配列: https://config.qmk.fm/#/crkbd/rev1/LAYOUT_split_3x6_3
  * 转换配列: [qmk_json2c_tool](/convert_tool/qmk_json2c_tool.html)
  * 复制文件到qmk库: `.\corne\copy-crkbd-vial.bat`
  * 下载虚拟环境: https://github.com/qmk/qmk_distro_msys/releases/tag/1.7.2
  * 编译固件: `qmk compile -kb crkbd -km vial -e CONVERT_TO=helios`
  * https://learn.adafruit.com/using-qmk-on-rp2040-microcontrollers/adafruit-kb2040-on-the-pb-gherkin-30-keyboard
  * https://docs.qmk.fm/#/platformdev_rp2040?id=rp2040_ce
## auto switch layer
  * https://github.com/hxse/py-active-windows-keyboard
