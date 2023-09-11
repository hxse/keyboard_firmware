copy /Y "D:\my_repo\keyboard_firmware\corne\vial-qmk\keyboards\crkbd\keymaps\vial\*.*" "D:\App\keyboard\vial-qmk\keyboards\crkbd\keymaps\vial\"
d:\App\keyboard\QMK_MSYS\qmk_msys\shell_connector.cmd -c 'cd D:/App/keyboard/vial-qmk;qmk compile -kb crkbd -km vial -e CONVERT_TO=helios'
