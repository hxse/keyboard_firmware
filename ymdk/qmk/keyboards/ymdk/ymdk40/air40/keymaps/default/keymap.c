/* Copyright 2022 Dennis Kruyt (dennis@kruyt.org)
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "raw_hid.h"

#include QMK_KEYBOARD_H
enum custom_keycodes {
    M_curly_brackets = SAFE_RANGE,
    M_square_brackets,
    M_round_brackets,
    M_angle_brackets,
    M_arrow_left,
    M_arrow_right,
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {[0] = LAYOUT_ortho_4x12_2x2u(KC_TAB, KC_Q, KC_W, KC_E, KC_R, KC_T, KC_Y, KC_U, KC_I, KC_O, KC_P, KC_ESC, KC_BSPC, KC_A, KC_S, KC_D, KC_F, KC_G, KC_H, KC_J, KC_K, KC_L, KC_COLN, KC_QUOT, KC_LSFT, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_N, KC_M, KC_COMM, KC_DOT, KC_EQL, KC_UNDS, TO(1), KC_0, KC_LALT, KC_LCTL, KC_SPC, KC_ENT, KC_LSFT, KC_LGUI, QK_BOOT, TG(1)),
                                                              [1] = LAYOUT_ortho_4x12_2x2u(KC_TAB, KC_Q, KC_W, KC_E, KC_R, KC_T, KC_Y, KC_U, KC_I, KC_O, KC_P, KC_ESC, KC_BSPC, KC_A, KC_S, KC_D, KC_F, KC_G, KC_H, KC_J, KC_K, KC_L, KC_COLN, KC_QUOT, LCTL(KC_Z), KC_Z, KC_X, KC_C, KC_V, KC_B, KC_N, KC_M, KC_COMM, KC_DOT, KC_EQL, KC_UNDS, OSL(4), KC_1, KC_LALT, KC_LCTL, LT(2, KC_SPC), LT(3, KC_ENT), KC_LSFT, KC_LGUI, KC_TRNS, KC_TRNS),
                                                              [2] = LAYOUT_ortho_4x12_2x2u(LALT(KC_TAB), LALT(LSFT(KC_F1)), LCTL(KC_LEFT), KC_UP, LCTL(KC_RGHT), KC_PGUP, KC_WH_U, KC_LCBR, KC_LBRC, KC_LPRN, KC_LT, KC_ESC, KC_DEL, LCTL(KC_LBRC), KC_LEFT, KC_DOWN, KC_RGHT, LCTL(KC_RBRC), KC_MUTE, KC_BTN1, KC_BTN3, KC_BTN2, KC_SCLN, KC_GRV, LCTL(LSFT(KC_Z)), LALT(LSFT(KC_F2)), KC_HOME, KC_INS, KC_END, KC_PGDN, KC_WH_D, KC_EXLM, KC_VOLD, KC_VOLU, KC_QUES, KC_UNDS, KC_NO, KC_2, KC_NO, KC_NO, KC_NO, LSFT(KC_ENT), KC_NO, KC_NO, KC_TRNS, KC_TRNS),
                                                              [3] = LAYOUT_ortho_4x12_2x2u(LCTL(KC_TAB), KC_PLUS, KC_MINS, KC_ASTR, KC_PERC, KC_AMPR, KC_PIPE, KC_RCBR, KC_RBRC, KC_RPRN, KC_GT, KC_ESC, KC_BSPC, KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7, KC_8, KC_9, KC_0, KC_DQUO, LCTL(KC_Z), KC_AT, KC_UNDS, KC_HASH, KC_TILD, KC_CIRC, KC_DLR, KC_BSLS, KC_COMM, KC_DOT, KC_SLSH, KC_UNDS, KC_NO, KC_3, KC_NO, KC_NO, LGUI(KC_SPC), KC_NO, KC_NO, KC_NO, KC_TRNS, KC_TRNS),
                                                              [4] = LAYOUT_ortho_4x12_2x2u(KC_NO, KC_F11, KC_F12, LCTL(LALT(LSFT(KC_F1))), LCTL(LALT(LSFT(KC_F2))), LCTL(LALT(LSFT(KC_F3))), LCTL(LSFT(KC_Y)), M_curly_brackets, M_square_brackets, M_round_brackets, M_angle_brackets, KC_NO, KC_NO, KC_F1, KC_F2, KC_F3, KC_F4, KC_F5, LCTL(LSFT(KC_H)), LCTL(LSFT(KC_J)), LCTL(LSFT(KC_K)), LCTL(LSFT(KC_L)), LCTL(LSFT(KC_SEMICOLON)), LCTL(LSFT(KC_QUOTE)), KC_NO, KC_F6, KC_F7, KC_F8, KC_F9, KC_F10, LCTL(LSFT(KC_N)), LCTL(LSFT(KC_M)), M_arrow_left, M_arrow_right, LCTL(LSFT(KC_SEMICOLON)), KC_NO, KC_NO, KC_4, KC_LALT, KC_LCTL, LCTL(LALT(LSFT(KC_F7))), LCTL(LALT(LSFT(KC_F8))), KC_LSFT, KC_LGUI, KC_TRNS, KC_TRNS)};

void keyboard_post_init_user(void) {
    // Customise these values to desired behaviour
    debug_enable = true;
    debug_matrix = true;
    // debug_keyboard=true;
    // debug_mouse=true;
    layer_move(1);
};

#ifdef RAW_ENABLE
void raw_hid_receive(uint8_t* data, uint8_t length) {
    // switch (data[0]) {
    //     case 0:
    //         data[5] = 0;
    //         break;
    //     case 1:
    //         data[5] = 1;
    //         break;
    //     case 2:
    //         data[5] = 2;
    //         break;
    //     case 104:
    //         data[5] = 106;
    //         break;
    // }
    // layer_clear();
    if (data[0] == 1) {
        // default_layer_set(data[1]);
        layer_move(data[1]);
    }
    raw_hid_send(data, length);
}
#endif

bool process_record_user(uint16_t keycode, keyrecord_t* record) {
    if (record->event.pressed) {
        switch (keycode) {
            case M_curly_brackets:
                SEND_STRING("{}" SS_TAP(X_LEFT));
                return false;
                break;
            case M_square_brackets:
                SEND_STRING("[]" SS_TAP(X_LEFT));
                return false;
                break;
            case M_round_brackets:
                SEND_STRING("()" SS_TAP(X_LEFT));
                return false;
                break;
            case M_angle_brackets:
                SEND_STRING("<>" SS_TAP(X_LEFT));
                return false;
                break;
            case M_arrow_left:
                SEND_STRING("<=");
                return false;
                break;
            case M_arrow_right:
                SEND_STRING("=>");
                return false;
                break;
        }
    }

#ifdef CONSOLE_ENABLE
    // uprintf("KL: kc: 0x%04X, col: %2u, row: %2u, pressed: %u, time: %5u, int: %u, count: %u\n", keycode, record->event.key.col, record->event.key.row, record->event.pressed, record->event.time, record->tap.interrupted, record->tap.count);
#endif
    return true;
};
