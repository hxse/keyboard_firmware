from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.handlers.sequences import send_string

CBR_COMBOS = M_curly_brackets = simple_key_sequence((send_string("{}"), KC.LEFT))
BRC_COMBOS = M_square_brackets = simple_key_sequence((send_string("[]"), KC.LEFT))
PRN_COMBOS = M_round_brackets = simple_key_sequence((send_string("()"), KC.LEFT))
ABK_COMBOS = M_angle_brackets = simple_key_sequence((send_string("<>"), KC.LEFT))
ARROW_LEFT = M_arrow_left = send_string("=>")
ARROW_RIGHT = M_arrow_right = send_string("<=")

QK_BOOT = KC.RESET

tap_time = 1500

OSL = lambda n: KC.OS(KC.TT(n), tap_time=tap_time)

OSM = lambda x: KC.OS(x, tap_time=tap_time)

RGB_TOG = KC.RGB_TOG
RGB_HUI = KC.RGB_HUI
RGB_HUD = KC.RGB_HUD
RGB_SAI = KC.RGB_SAI
RGB_SAD = KC.RGB_SAD
RGB_VAI = KC.RGB_VAI
RGB_VAD = KC.RGB_VAD


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
        KC.SCLN,
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
        OSL(4),
        OSL(5),
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
        OSM(KC.LALT),
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
        OSM(KC.LCTL),
        KC.LT(2, KC.SPC),
        KC.LT(4, KC.ENT),
        OSL(5),
        KC.LT(3, KC.ENT),
        KC.LSFT,
    ],
    [
        KC.LALT(KC.TAB),
        KC.LALT(KC.LSFT(KC.F9)),
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
        KC.LT(5, KC.ENT),
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
        KC.LSFT,
        KC.LCTL(KC.LSFT(KC.Z)),
        KC.HOME,
        KC.LALT(KC.LSFT(KC.F6)),
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
        KC.LSFT(KC.ENT),
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
        KC.LALT(KC.LSFT(KC.F7)),
        KC.F11,
        KC.F12,
        KC.LALT(KC.LSFT(KC.F3)),
        KC.LALT(KC.LSFT(KC.F4)),
        KC.LALT(KC.LSFT(KC.F5)),
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.TRNS,
        KC.LALT(KC.LSFT(KC.F8)),
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
        KC.TRNS,
        KC.TRNS,
        KC.TO(1),
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.TRNS,
        KC.NO,
        KC.N1,
        KC.N2,
        KC.N3,
        KC.N0,
        KC.NO,
        M_curly_brackets,
        M_square_brackets,
        M_round_brackets,
        M_angle_brackets,
        KC.TRNS,
        KC.NO,
        KC.NO,
        KC.N4,
        KC.N5,
        KC.N6,
        KC.LCTL(KC.LBRC),
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.MO(6),
        KC.NO,
        KC.TRNS,
        KC.NO,
        KC.N7,
        KC.N8,
        KC.N9,
        KC.DOT,
        KC.NO,
        KC.NO,
        M_arrow_left,
        M_arrow_right,
        KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        QK_BOOT,
        KC.TO(1),
        KC.TO(0),
        KC.NO,
    ],
    [
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        QK_BOOT,
        RGB_HUD,
        RGB_VAI,
        RGB_HUI,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        RGB_TOG,
        RGB_SAD,
        RGB_VAD,
        RGB_SAI,
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
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
    ],
]
