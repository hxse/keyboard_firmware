# keyboard_firmware
## qmk firmware
  * 因为hid和via有点冲突, 所以不开via, https://github.com/vial-kb/vial-qmk/issues/538
  * `git clone https://github.com/qmk/qmk_firmware`
  * https://github.com/qmk/qmk_distro_msys/releases/tag/1.7.2
  * `qmk compile -kb crkbd/rev1 -km hxse_firmware -e CONVERT_TO=helios`
