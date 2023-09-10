from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.handlers.sequences import send_string

CBR_COMBOS = simple_key_sequence((send_string("{}"), KC.LEFT))
BRC_COMBOS = simple_key_sequence((send_string("[]"), KC.LEFT))
PRN_COMBOS = simple_key_sequence((send_string("()"), KC.LEFT))
ABK_COMBOS = simple_key_sequence((send_string("<>"), KC.LEFT))
ARROW_COMBOS = send_string("=>")

tap_time = 1500


OS_L = KC.OS(KC.TT(4), tap_time=tap_time)
OS_R = KC.OS(KC.TT(5), tap_time=tap_time)

OS_LCTL = KC.OS(KC.LCTL, tap_time=tap_time)
OS_LSFT = KC.OS(KC.LSFT, tap_time=tap_time)
OS_LALT = KC.OS(KC.LALT, tap_time=tap_time)
OS_LGUI = KC.OS(KC.LGUI, tap_time=tap_time)


keymap = [
    [
        KC.TAB,
        KC.Q,
        KC.W,
        KC.E,
        KC.R,
        KC.T,
        KC.Y,
        KC.U,
        KC.I,
        KC.O,
        KC.P,
        KC.ESC,
        KC.BSPC,
        KC.A,
        KC.S,
        KC.D,
        KC.F,
        KC.G,
        KC.H,
        KC.J,
        KC.K,
        KC.L,
        KC.COLN,
        KC.QUOT,
        KC.LALT,
        KC.Z,
        KC.X,
        KC.C,
        KC.V,
        KC.B,
        KC.N,
        KC.M,
        KC.COMM,
        KC.DOT,
        KC.EQL,
        KC.LGUI,
        KC.LCTL,
        KC.SPC,
        OS_L,
        OS_R,
        KC.ENT,
        KC.LSFT,
    ],
    [
        KC.TAB,
        KC.Q,
        KC.W,
        KC.E,
        KC.R,
        KC.T,
        KC.Y,
        KC.U,
        KC.I,
        KC.O,
        KC.P,
        KC.ESC,
        KC.BSPC,
        KC.A,
        KC.S,
        KC.D,
        KC.F,
        KC.G,
        KC.H,
        KC.J,
        KC.K,
        KC.L,
        KC.LSFT(KC.SCLN),
        KC.QUOT,
        OS_LALT,
        KC.Z,
        KC.X,
        KC.C,
        KC.V,
        KC.B,
        KC.N,
        KC.M,
        KC.COMM,
        KC.DOT,
        KC.EQL,
        OS_LGUI,
        OS_LCTL,
        KC.LT(2, KC.SPC),
        OS_L,
        OS_R,
        KC.LT(3, KC.ENT),
        KC.LSFT,
    ],
    [
        KC.LCTL(KC.LALT(KC.TAB)),
        KC.LALT,
        KC.LCTL(KC.LEFT),
        KC.UP,
        KC.LCTL(KC.RGHT),
        KC.PGUP,
        KC.NO,
        KC.LCBR,
        KC.LBRC,
        KC.LPRN,
        KC.LABK,
        KC.TRNS,
        KC.DEL,
        KC.LCTL(KC.LBRC),
        KC.LEFT,
        KC.DOWN,
        KC.RGHT,
        KC.LCTL(KC.RBRC),
        KC.MUTE,
        KC.MB_LMB,
        KC.MB_MMB,
        KC.MB_RMB,
        KC.SCLN,
        KC.GRV,
        KC.TRNS,
        KC.LCTL(KC.LSFT(KC.Z)),
        KC.HOME,
        KC.TO(0),
        KC.END,
        KC.PGDN,
        KC.NO,
        KC.EXLM,
        KC.VOLD,
        KC.VOLU,
        KC.QUES,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.TRNS,
        KC.PLUS,
        KC.MINS,
        KC.ASTR,
        KC.PERC,
        KC.AMPR,
        KC.PIPE,
        KC.RCBR,
        KC.RBRC,
        KC.RPRN,
        KC.RABK,
        KC.TRNS,
        KC.TRNS,
        KC.N1,
        KC.N2,
        KC.N3,
        KC.N4,
        KC.N5,
        KC.N6,
        KC.N7,
        KC.N8,
        KC.N9,
        KC.N0,
        KC.DQUO,
        KC.TRNS,
        KC.AT,
        KC.UNDS,
        KC.HASH,
        KC.TILD,
        KC.CIRC,
        KC.DLR,
        KC.BSLS,
        KC.COMM,
        KC.DOT,
        KC.SLSH,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.LCTL(KC.LALT(KC.LSFT(KC.F7))),
        KC.F6,
        KC.F7,
        KC.F8,
        KC.F9,
        KC.F10,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.TRNS,
        KC.LCTL(KC.LALT(KC.LSFT(KC.F8))),
        KC.F1,
        KC.F2,
        KC.F3,
        KC.F4,
        KC.F5,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.TRNS,
        KC.F11,
        KC.F12,
        KC.LCTL(KC.LALT(KC.F3)),
        KC.LCTL(KC.LALT(KC.F4)),
        KC.LCTL(KC.LALT(KC.F5)),
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.ENT,
        KC.TO(1),
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.TRNS,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        CBR_COMBOS,
        BRC_COMBOS,
        PRN_COMBOS,
        ABK_COMBOS,
        KC.TRNS,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        ARROW_COMBOS,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.TRNS,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TO(1),
        KC.TRNS,
        KC.TRNS,
    ],
]
